import os

import pandas as pd
import streamlit as st

from utils.csv_agent_utils import dataframe_agent
from utils.streamlit_utils import human_message


def create_chart(input_data, chart_type):
	df_data = pd.DataFrame(input_data["data"], columns=input_data["columns"])
	df_data.set_index(input_data["columns"][0], inplace=True)
	if chart_type == "bar":
		st.bar_chart(df_data)
	elif chart_type == "line":
		st.line_chart(df_data)
	elif chart_type == "scatter":
		st.scatter_chart(df_data)


st.title('📊CSV Analysis Tool')

uploaded_file = st.file_uploader("Upload a CSV file", type=[".csv"])

with st.sidebar:
	api_key = st.text_input("Please input your api key", type="password", value=os.getenv("OPENAI_API_KEY"))
	if not api_key:
		st.warning("Please input your api key")
if uploaded_file:
	st.session_state["csv_df"] = pd.read_csv(uploaded_file)
	with st.expander("Original Data"):
		st.dataframe(st.session_state["csv_df"])
query = st.text_area("Please input question about the file you've uploaded, AI can generate bar/line/scatter charts：")
button = st.button("Get Answer")
if query:
	if not api_key:
		st.warning("Please input your api key")
		st.stop()
	if not uploaded_file:
		st.warning("Please upload a CSV file")
		st.stop()
	with st.spinner('AI is thinking, please wait...'):
		# get Answer here
		response_dict = dataframe_agent(api_key, st.session_state["csv_df"], query)
		if "answer" in response_dict:
			st.write(response_dict["answer"])
		if "table" in response_dict:
			st.table(pd.DataFrame(response_dict["table"]["data"],
								  columns=response_dict["table"]["columns"]))
		if "bar" in response_dict:
			create_chart(response_dict["bar"], "bar")
		if "line" in response_dict:
			create_chart(response_dict["line"], "line")
		if "scatter" in response_dict:
			create_chart(response_dict["scatter"], "scatter")
