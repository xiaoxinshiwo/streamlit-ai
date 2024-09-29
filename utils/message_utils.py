import streamlit as st


def ai_message(message):
	return st.chat_message(name="ai", avatar="image/robot.png").write(message)


def human_message(message):
	return st.chat_message(name="human", avatar="image/human.png").write(message)
