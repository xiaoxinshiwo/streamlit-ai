import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils.ppm_help_utils import PPMHelper
from utils.streamlit_utils import ai_message, human_message, openai_key_side_bar

st.subheader('📚Chat with PPM online document')

api_key = openai_key_side_bar()

ai_message("Hello, I'm your PPM AI assistant. How Can I help?")

query = st.chat_input()
if 'chat_message_ppm' not in st.session_state:
	st.session_state.chat_message_ppm = []
	st.session_state.memory_ppm = ConversationBufferMemory(return_messages=True, memory_key="chat_history",
														   output_key="answer")

for message in st.session_state.chat_message_ppm:
	human_message(message['query'])
	ai_message(message['answer'])

if query:
	if not api_key:
		st.warning("Please input your api key")
		st.stop()
	human_message(query)
	with st.spinner('AI is thinking, please wait...'):
		# get Answer here
		ppm = PPMHelper(question=query, memory=st.session_state.memory_ppm, api_key=api_key)
		try:
			ppm.invoke()
			answer = ppm.answer
		except Exception as e:
			answer = e
		ai_message(answer)
		st.session_state.chat_message_ppm.append({'query': query, 'answer': answer})
