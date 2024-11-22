import os
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
			agent=agent, tools=tools, verbose=True, handle_parsing_errors=True, early_stopping_method="generate"
		)
		response = agent_executor.invoke({"input": automation_prompt.auto_prompt + test_steps})
		markdown_resp = f"""
		```typescript
		{response['output']}
		"""
	except Exception as error:
		print(error)
		raise Exception("Generate test case failed, please try again.")
	return markdown_resp


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
	3. 选择 id=WORKFLOW_IDAUTOCOMP_IMG 的 single ACL，值为 Auto_DM_Risk_Prosess
	4. 选择 id=REQ.DEPARTMENT_CODE 的下拉框的选项 Finance
	5. 选择 id=REQ.PRIORITY_CODE 的下拉框的选项 Low
	6. 选择 id=REQD.P.MODULE 的下拉框的选项 Module A
	7. 选择 id=REQD.P.IMPACT 的下拉框的选项 Severe
	8. 选择 id=REQD.P.PLATFORM 的下拉框的选项 Linux
	9. 填充 id=REQ.DESCRIPTION 的文本框的值为 'This is a debug lib type'
	10. 点击 id=REQD.P.REPRO_Y 的 radio button
	11. 添加 note，内容为：This is a testing lib
	12. var req_id = 提交请求
	13. 删除请求req_id
	"""
	resp = write_ppm_automation(test_context, os.getenv('OPENAI_API_KEY'))
	print(resp)
