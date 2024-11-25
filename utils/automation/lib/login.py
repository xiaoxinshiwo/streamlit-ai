from langchain_core.tools import BaseTool

from utils.automation.base_lib_class import BaseLibClass


class Login(BaseTool):
	name: str = "Tool to login"
	description: str = (
		'Use this tool when you are asked to login'
	)
	return_direct: bool = True

	def _run(self):
		return 'await login(page, PPMURL,"admin","admin");'

class LoginLogout(BaseLibClass):
	@staticmethod
	def get_tools():
		return [Login()]
