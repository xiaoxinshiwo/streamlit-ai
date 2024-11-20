import os

import streamlit as st

from utils import agent_utils

st.title('📖PPM ui automation')

with st.sidebar:
	api_key = st.text_input("Please input your api key", type="password", value=os.getenv("OPENAI_API_KEY"))
	if not api_key:
		st.warning("Please input your api key")

test_context = st.text_area(placeholder="Please input your test steps", label="Test Steps", height=400)

if test_context:
	if not api_key:
		st.warning("Please input your api key")
		st.stop()
	with st.spinner('AI is thinking, please wait...'):
		# get Answer here
		test_case = agent_utils.write_ppm_automation(test_context, api_key)
		print('test_case===', test_case)
		st.markdown(test_case)
