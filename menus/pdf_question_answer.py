import os

import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils.AIUtils import pdf_qa_agent
from utils.messageUtils import AIMessage, HumanMessage

st.title('Upload PDF and ask questions')

with st.expander("RAG(Retrieval augmented generation)"):
	st.image("image/RAG_diagram.svg")
	st.markdown(
		"Refer to : [Retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)")

uploaded_file = st.file_uploader("Upload a PDF file", type=[".pdf"])

with st.sidebar:
	api_key = st.text_input("Please input your api key", type="password", value=os.getenv("OPENAI_API_KEY"))
	if not api_key:
		st.warning("Please input your api key")

AIMessage("Hello, I'm your AI assistant. Please upload a PDF, I can find answers from it.")

query = st.chat_input()
if 'chat_message_pdf' not in st.session_state:
	st.session_state.chat_message_pdf = []
	st.session_state.memory_pdf = ConversationBufferMemory(return_messages=True, memory_key="chat_history",
														   output_key="answer")

for message in st.session_state.chat_message_pdf:
	HumanMessage(message['query'])
	AIMessage(message['answer'])

if query:
	if not api_key:
		st.warning("Please input your api key")
		st.stop()
	if not uploaded_file:
		st.warning("Please upload a PDF file")
	HumanMessage(query)
	with st.spinner('AI is thinking, please wait...'):
		# get Answer here
		answer = pdf_qa_agent(question=query,
							  memory=st.session_state.memory_pdf,
							  openai_api_key=api_key,
							  uploaded_file=uploaded_file)
		AIMessage(answer)
		st.session_state.chat_message_pdf.append({'query': query, 'answer': answer})
