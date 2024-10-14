import streamlit as st

pages = {
	"CHAT": [
		st.Page("menus/chat_without_memory.py", title="Chat without memory"),
		st.Page("menus/chat_with_memory.py", title="Chat with memory"),
	],
	"RAG": [
		st.Page("menus/pdf_question_answer.py", title="Upload PDF and ask questions"),
		st.Page("menus/ppm_help_document.py", title="Get help for PPM"),
	],
	"AGENT": [
		st.Page("menus/python_executor.py", title="Python Tools"),
		st.Page("menus/csv_analysis_tool.py", title="CSV Tools"),
		st.Page("menus/calculate_character_number.py", title="Calculate character number"),
		st.Page("menus/agent_tools.py", title="Tools"),
	],
}

st.set_page_config(
	page_icon="image/AI.png",
	layout="wide",
	initial_sidebar_state="expanded",
)

pg = st.navigation(pages)
pg.run()
