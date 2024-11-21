import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils.agent_utils import get_strawberry_answer
from utils.streamlit_utils import ai_message, human_message, openai_key_side_bar

# examples:
# 在句子“山重水复疑无路，柳暗花明又一村”中有多少个汉字？\n
# 请问strawberry这个单词中有多少个字符r?

st.subheader('🍓Calculate character number')

api_key = openai_key_side_bar()
ai_message("Hello, I'm your AI assistant. How Can I help?")
query = st.chat_input()

if 'chat_message_strawberry' not in st.session_state:
	st.session_state.chat_message_strawberry = []
	st.session_state.memory_strawberry = ConversationBufferMemory(
		memory_key='chat_history',
		return_messages=True
	)

for message in st.session_state.chat_message_strawberry:
	human_message(message['query'])
	ai_message(message['answer'])

if query:
	if not api_key:
		st.warning("Please input your api key")
		st.stop()
	human_message(query)
	with st.spinner('AI is thinking, please wait...'):
		# get Answer here
		answer = get_strawberry_answer(query, st.session_state.memory_strawberry, api_key)['output']
		ai_message(answer)
		st.session_state.chat_message_strawberry.append({'query': query, 'answer': answer})
