import streamlit as st

from utils.automation import automation_agent
from utils.streamlit_utils import openai_key_side_bar

st.subheader('📝PPM ui automation')

api_key = openai_key_side_bar()
with st.expander("Examples"):
	st.markdown(
		"""
		```code
		1. 登录
		2. 创建一个类型为 'Bug' 的请求
		3. 选择 id=WORKFLOW_IDAUTOCOMP_IMG 的 single ACL，值为 Auto_DM_Risk_Prosess
		4. 选择 id=REQ.DEPARTMENT_CODE 的下拉框的选项 Finance
		5. 选择 id=REQ.PRIORITY_CODE 的下拉框的选项 Low
		6. 选择 id=REQD.P.MODULE 的下拉框的选项 Module A
		7. 选择 id=REQD.P.IMPACT 的下拉框的选项 Severe
		8. 选择 id=REQD.P.PLATFORM 的下拉框的选项 Linux
		9. 填充 id=REQ.DESCRIPTION 的文本框的值为 'This is a debug request type'
		10. 点击 id=REQD.P.REPRO_Y 的 radio button
		11. 添加 note，内容为：This is a testing request
		12. var req_id = 提交请求
		13. 删除请求req_id
		```
		"""
	)
editor_col, code_col = st.columns(2)
test_case = ''
with editor_col:
	test_steps = st.text_area(placeholder="Please input your test steps.", label="Test Steps", height=400)
	generate = st.button("Generate", icon=":material/play_arrow:")
	if generate:
		if test_steps:
			if not api_key:
				st.warning("Please input your api key.")
				st.stop()
			with st.spinner('AI is thinking, please wait...'):
				# get Answer here
				try:
					test_case = automation_agent.write_ppm_automation(test_steps, api_key)
				except Exception as e:
					st.warning(e)
				print('test_case===', test_case)
		else:
			st.warning("Please input your test steps.")
with code_col:
	if test_case:
		st.markdown(test_case)
