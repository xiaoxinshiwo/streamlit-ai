import streamlit as st


def AIMessage(message):
	return st.chat_message(name="ai", avatar="image/robot.png").write(message)


def HumanMessage(message):
	return st.chat_message(name="human", avatar="image/human.png").write(message)
