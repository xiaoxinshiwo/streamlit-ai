import streamlit as st

from utils import agent_utils
from utils.streamlit_utils import openai_key_side_bar

st.title('📖PPM ui automation')

api_key = openai_key_side_bar()
test_context = st.text_area(placeholder="Please input your test steps.", label="Test Steps", height=400, label_visibility="hidden")
if st.button("Generate", type="primary"):

	if test_context:
		if not api_key:
			st.warning("Please input your api key.")
			st.stop()
		with st.spinner('AI is thinking, please wait...'):
			# get Answer here
			test_case = agent_utils.write_ppm_automation(test_context, api_key)
			print('test_case===', test_case)
			st.markdown(test_case)
	else:
		st.warning("Please input your test steps.")
