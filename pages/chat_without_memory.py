import os

import streamlit as st

from utils.AIUtils import get_chat_response
from utils.messageUtils import AIMessage, HumanMessage


st.title('Chat without memory')

with st.sidebar:
	api_key = st.text_input("Please input your api key", type="password", value=os.getenv("OPENAI_API_KEY"))
	if not api_key:
		st.warning("Please input your api key")

AIMessage("Hello, I'm your AI assistant. How Can I help?")

query = st.chat_input()
if 'chat_message_cwom' not in st.session_state:
	st.session_state.chat_message_cwom = []

for message in st.session_state.chat_message_cwom:
	HumanMessage(message['query'])
	AIMessage(message['answer'])

if query:
	if not api_key:
		st.warning("Please input your api key")
		st.stop()
	HumanMessage(query)
	with st.spinner('AI is thinking, please wait...'):
		# get Answer here
		answer = get_chat_response(prompt=query, openai_api_key=api_key)
		AIMessage(answer)
		st.session_state.chat_message_cwom.append({'query': query, 'answer': answer})
