import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils.agent_utils import python_executor
from utils.streamlit_utils import openai_key_side_bar

st.subheader("💻Python Executor")

api_key = openai_key_side_bar()

question = st.text_area(placeholder="Please input your question", label="Question", height=100)
button = st.button("submit")
if button and not question:
	st.warning("Please input your question ")
	st.stop()

if button and question:
	with st.spinner('AI is thinking, please wait...'):
		answer = python_executor(api_key=api_key, question=question, memory=None)
		st.write(answer["output"])
