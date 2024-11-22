from langchain_core.tools import BaseTool


class Login(BaseTool):
	name: str = "Tool to generate code to login"
	description: str = (
		'Use this tool when you are asked to login, need to import dependencies: import {login} from "@lib/Login"; import {PPMURL} from "@config";'
	)

	def _run(self):
		return 'await login(page, PPMURL,"admin","admin");'


class LoginLogout:
	@staticmethod
	def get_tools():
		return [Login()]
