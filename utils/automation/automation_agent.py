import os
import re
import time
import streamlit as st
from itertools import chain
from typing import Sequence, Type, List

from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain_openai import ChatOpenAI

from utils.automation import automation_prompt
from utils.automation.lib.ctrls import Ctrls
from utils.automation.lib.login import LoginLogout
from utils.automation.lib.menus import Menus
from utils.automation.lib.requests import *
from utils.automation.lib.selector import Selector


def write_ppm_automation(test_steps, api_key):
	time_begin = time.time()
	steps = [line for line in test_steps.splitlines() if line.strip()]
	code_format = """
	test('Automated Test Case', async ({ page }) => {
	   CODE_BLOCK
	});
	"""
	code_lines = []
	placeholder = st.empty()
	for step in steps:
		with placeholder.container():
			st.write(f"`{step}`")
		code_lines.append(f"// {step}")
		var1, var2 = param_assignment(test_step=step)
		code_line = single_step_agent(var2, api_key)
		if var1:
			code_line = var1 + code_line
		code_lines.append(code_line)
	code_to_format = code_format.replace('CODE_BLOCK', "\n".join(code_lines))
	with placeholder.container():
		st.write(f"`Last step, organize imports and formatting`")
	final_code = formats_and_imports(api_key, code_to_format)
	time_end = time.time()
	total_cost = '🎉Test case generated successfully! Total cost: `{:.3f} ms` \n'.format((time_end - time_begin) * 1000.0)
	with placeholder.container():
		st.write(total_cost)
	return final_code


def param_assignment(test_step):
	"""
	Process a test step with an assignment and extract the variable assignment and the assigned value.

	Examples of input:
		"var req_id = 提交请求"
		"const req_id = 提交请求"
		"let req_id = 提交请求"

	:param test_step: str, a string containing the test step
	:return: tuple ("var req_id =", "提交请求")
	"""
	# Define a regex pattern to match variable assignments
	cleaned_step = re.sub(r".*?\b(var|const|let)\b", r"\1", test_step.strip())
	pattern = r".*?(var|const|let)\s+\w+\s*=\s*(.+)"
	match = re.match(pattern, cleaned_step.strip())

	if match:
		assignment_part = match.group(0).split("=")[0].strip() + " ="
		value_part = match.group(2).strip()
		return assignment_part, value_part

	return False, test_step


def formats_and_imports(openai_api_key, code_to_format):
	model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key)
	response = model.invoke(automation_prompt.format_prompt + code_to_format)
	return response.content


def single_step_agent(test_step, api_key):
	model = ChatOpenAI(api_key=api_key, model="gpt-4o-mini", temperature=0)
	tools = list_all_tools([Ctrls, LoginLogout, Requests, Menus, Selector])
	prompt = automation_prompt.agent_prompt

	agent = create_structured_chat_agent(
		llm=model,
		tools=tools,
		prompt=prompt
	)
	try:
		agent_executor = AgentExecutor.from_agent_and_tools(
			agent=agent, tools=tools, verbose=True, handle_parsing_errors=True, early_stopping_method="generate",
			max_iterations=2
		)
		response = agent_executor.invoke({"input": automation_prompt.auto_prompt + test_step})
	except Exception as error:
		print(error)
		response = {'output': f"// Note Generate test case failed, will skip it."}
	return response['output']


def list_all_tools(class_array: (Sequence[Type[BaseLibClass]])) -> List[BaseTool]:
	"""Returns a list of instances of classes that inherit from BaseTool.
	Args:
		class_array (Sequence[Type[BaseLibClass]]): A sequence of classes.
	Returns:
		List[BaseTool]: A list of BaseTool instances.
	"""
	return list(chain.from_iterable(clazz.get_tools() for clazz in class_array))


if __name__ == '__main__':
	proxy = os.getenv("SYSTEM_PROXY")
	if proxy:
		# set global proxy
		os.environ['http_proxy'] = proxy
		os.environ['https_proxy'] = proxy
	test_context = """
	1. 登录
	2. 创建一个类型为 'Bug' 的请求
	3. 选择 id=WORKFLOW_IDAUTOCOMP_IMG 的 single ACL, 值为 Auto_DM_Risk_Prosess
	4. 选择 id=REQ.DEPARTMENT_CODE 的下拉框的选项 Finance
	5. 选择 id=REQ.PRIORITY_CODE 的下拉框的选项 Low
	6. 选择 id=REQD.P.MODULE 的下拉框的选项 Module A
	7. 选择 id=REQD.P.IMPACT 的下拉框的选项 Severe
	8. 选择 id=REQD.P.PLATFORM 的下拉框的选项 Linux
	9. 填充 id=REQ.DESCRIPTION 的文本框的值为 'This is a debug request type'
	10. 点击 id=REQD.P.REPRO_Y 的 radio button
	11. 添加 note, 内容为：This is a testing request
	12. var req_id = 提交请求
	13. 删除请求req_id
	"""
	resp = write_ppm_automation(test_context, os.getenv('OPENAI_API_KEY'))
	print(resp)
