"""
Tool for PPM help to retrieve answers from questions
1. search by key word
2. find the perfect matched url by embedding LLM
3. fetch the content from matched url
4. summarize by LLM
example:
	question = 'how to create a request from Create menu?'
	question = 'how to customize PPM menu, and how to delete one?'
	question = "what's PPM?"

Langchain document:
https://python.langchain.com/docs/how_to/qa_sources/#using-create_retrieval_chain
"""
import base64
import json
import os
import re
from urllib.parse import urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import RecursiveUrlLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


def get_authorization():
	key = "697:8942:SearchKey"
	# The input needs to be a bytes-like object, so you encode the string first
	encoded = base64.b64encode(key.encode('utf-8'))
	# Convert the bytes object back to a string
	site_key = encoded.decode('utf-8')
	return f"SiteKey {site_key}"


def bs4_extractor(html: str) -> str:
	soup = BeautifulSoup(html, "lxml")
	return re.sub(r"\n\n+", "\n\n", soup.text).strip()


def recursive_load(page_url):
	loader = RecursiveUrlLoader(page_url, extractor=bs4_extractor)
	docs = loader.load()
	# for doc in docs:
	# 	print(doc.page_content)
	return docs


def get_title_link(html_content):
	# 解析HTML
	soup = BeautifulSoup(html_content, 'html.parser')
	results = []
	existing_titles = []
	for a_tag in soup.find_all('a', title=True, href=True):
		title = a_tag['title']
		url = a_tag['href']
		parsed_url = urlsplit(url)
		# remove parameters
		url_without_params = urlunsplit((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', ''))
		result = {
			'title': title,
			'url': url_without_params
		}
		if title not in existing_titles:
			existing_titles.append(title)
			results.append(str(result))

	return results


class PPMHelper:
	def __init__(self, memory, api_key, question):
		self.memory = memory
		self.api_key = api_key
		self.question = question
		self.page_url = ""
		self.answer = ""

	# get final answer
	def final_answer(self):
		docs = recursive_load(self.page_url)
		embeddings_model = OpenAIEmbeddings(api_key=self.api_key)
		db = FAISS.from_documents(documents=docs, embedding=embeddings_model)
		retriever = db.as_retriever()
		prompt = f'''
			Please find the answer according to the context. Please give an answer with steps to follow.
			If you can't find the answer, you can return the url:{self.page_url} for users to refer to.
			Question is:{self.question}
		'''
		return self.embedding_llm_invoke(prompt, self.memory, retriever, 'map_reduce')

	def key_word_search(self):
		url = 'https://api.cludo.com/api/v3/697/8942/search'
		data = '''
			{
			"ResponseType": "JsonHtml",
			"Template": "SearchContent",
			"facets": {
				"Category": [
					"PPM"
				],
				"TopCategory": [],
				"SubCategory": [],
				"HostSite": []
			},
			"filters": {},
			"page": 1,
			"query": "#question#",
			"text": "",
			"traits": [],
			"sort": {},
			"rangeFacets": {},
			"perPage": 100,
			"enableRelatedSearches": true,
			"applyMultiLevelFacets": true
		}
		'''
		data = data.replace('#question#', self.question)
		try:
			response = requests.post(
				url=url,
				headers={"authorization": get_authorization(), "content-type": "application/json;charset=UTF-8"},
				data=data
			)
			if response.status_code != 200:
				return []
			cleaned_content = response.content.decode('utf-8').replace("\\r", '').replace('\\n', '').replace(
				'\\t', '')
			search_result = json.loads(cleaned_content).get('SearchResult')
			result = get_title_link(search_result)
			return result
		except requests.exceptions.RequestException as e:
			print(f"Error accessing the URL: {e}")
			return []

	def get_matched_link(self, search_result):
		embeddings_model = OpenAIEmbeddings(api_key=self.api_key)
		db = FAISS.from_texts(texts=search_result, embedding=embeddings_model)
		retriever = db.as_retriever()
		prompt = f'''Please find the perfect matched item according to the context.
			Do not replay and append other words, only response with a website url, for example:
			https://admhelp.microfocus.com/ppm/en/24.1-24.3/Help/Content/UG/DMUG/create_req.htm
			Question is:{self.question}
		 '''
		self.page_url = self.embedding_llm_invoke(prompt, self.memory, retriever)

	def embedding_llm_invoke(self, prompt, memory, retriever, chain_type='stuff'):
		model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=self.api_key, temperature=0)
		qa = ConversationalRetrievalChain.from_llm(
			llm=model,
			retriever=retriever,
			memory=memory,
			chain_type=chain_type
		)
		response = qa.invoke({"chat_history": memory, "question": prompt})
		return response["answer"]

	# main entry
	def invoke(self):
		search_result = self.key_word_search()
		print("Get results count by keyword:", len(search_result))
		if not search_result:
			raise Exception('No answer found. Please describe your problem in detail and try again.')
		self.get_matched_link(search_result)
		print("Get perfect match url:\n", self.page_url)
		if not self.page_url:
			raise Exception('No answer found. Please describe your problem in detail and try again.')
		if not self.page_url.startswith("http"):
			# if not return the page url, this parameter itself is the answer
			self.answer = self.page_url
			return
		self.answer = self.final_answer() + "\n" + f"[More🔗]({self.page_url})"


if __name__ == '__main__':
	question = 'how to customize PPM menu, and how to delete one?'
	memory = ConversationBufferMemory(return_messages=True, memory_key="chat_history",
									  output_key="answer")
	api_key = os.getenv('OPENAI_API_KEY')
	answer = PPMHelper(question=question, memory=memory, api_key=api_key).invoke()
	print(answer)
