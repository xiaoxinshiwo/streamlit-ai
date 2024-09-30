import streamlit as st

from utils.agent_utils import python_executor
from utils.streamlit_utils import openai_key_side_bar

st.title("💻Python Executor")

api_key = openai_key_side_bar()

question = st.text_area(placeholder="Please input your question", label="Question")
button = st.button("submit")
if button and not question:
	st.warning("Please input your question ")
	st.stop()

if button and question:
	with st.spinner('AI is thinking, please wait...'):
		answer = python_executor(openai_api_key=api_key, prompt=question)["output"]
		st.write(answer)
