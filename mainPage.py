import streamlit as st

pages = {
	"Chat": [
		st.Page("pages/chat_without_memory.py", title="Chat without memory"),
		st.Page("pages/chat_with_memory.py", title="Chat with memory"),
	],
	# "tools": [
	#     st.Page("learn.py", title="Learn about us"),
	#     st.Page("trial.py", title="Try it out"),
	# ],
}

st.set_page_config(
	page_icon="image/AI.png",
	layout="wide",
	initial_sidebar_state="expanded",
)

pg = st.navigation(pages)
pg.run()
