from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI


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
