from langchain.chains import ConversationChain
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from utils.pdf_utils import read_uploaded_and_split_pdf


def get_chat_memory_response(prompt, memory, openai_api_key):
	model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key)
	chain = ConversationChain(llm=model, memory=memory)

	response = chain.invoke({"input": prompt})
	return response["response"]


def get_chat_response(prompt, openai_api_key):
	model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key)
	chain = ConversationChain(llm=model)

	response = chain.invoke({"input": prompt})
	return response["response"]


def pdf_qa_agent(openai_api_key, memory, uploaded_file, question):
	model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key)
	embeddings_model = OpenAIEmbeddings()
	texts = read_uploaded_and_split_pdf(uploaded_file)
	db = FAISS.from_documents(texts, embeddings_model)
	retriever = db.as_retriever()
	qa = ConversationalRetrievalChain.from_llm(
		llm=model,
		retriever=retriever,
		memory=memory
	)
	q_template = f'''Please answer according to the context. If the question is irrelevant to the context, please answer "I don't know".\n Question is:{question}'''

	response = qa.invoke({"chat_history": memory, "question": q_template})
	return response["answer"]
