import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils.agent_utils import get_tool_collection_answer
from utils.streamlit_utils import ai_message, human_message, openai_key_side_bar

st.title('🛠️Tool Collection')

api_key = openai_key_side_bar()

ai_message("Hello, I'm your AI assistant. How Can I help?")

query = st.chat_input()
if 'chat_message_tools' not in st.session_state:
	st.session_state.chat_message_tools = []
	st.session_state.memory_tools = ConversationBufferMemory(return_messages=True)

for message in st.session_state.chat_message_tools:
	human_message(message['query'])
	ai_message(message['answer'])

if query:
	if not api_key:
		st.warning("Please input your api key")
		st.stop()
	human_message(query)
	with st.spinner('AI is thinking, please wait...'):
		# get Answer here
		answer = get_tool_collection_answer(query, st.session_state.memory_tools, api_key)['output']
		ai_message(answer)
		st.session_state.chat_message_tools.append({'query': query, 'answer': answer})
