import streamlit as st

from utils.automation import automation_agent
from utils.streamlit_utils import openai_key_side_bar

st.subheader('📝PPM ui automation')

api_key = openai_key_side_bar()
editor_col, code_col = st.columns(2)
test_case = ''
with editor_col:
	test_context = st.text_area(placeholder="Please input your test steps.", label="Test Steps", height=400)
	generate = st.button("Generate", icon=":material/play_arrow:")
	if generate:
		if test_context:
			if not api_key:
				st.warning("Please input your api key.")
				st.stop()
			with st.spinner('AI is thinking, please wait...'):
				# get Answer here
				try:
					test_case = automation_agent.write_ppm_automation(test_context, api_key)
				except Exception as e:
					st.warning(e)
				print('test_case===', test_case)
		else:
			st.warning("Please input your test steps.")
with code_col:
	if test_case:
		st.markdown(test_case)
