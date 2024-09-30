import os

import streamlit as st


def ai_message(message):
	return st.chat_message(name="ai", avatar="image/robot.png").write(message)


def human_message(message):
	return st.chat_message(name="human", avatar="image/human.png").write(message)


def openai_key_side_bar():
	with st.sidebar:
		api_key = st.text_input("Please input your api key", type="password", value=os.getenv("OPENAI_API_KEY"))
		if not api_key:
			st.warning("Please input your api key")

	return api_key
