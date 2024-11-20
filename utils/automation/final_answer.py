from langchain_core.tools import BaseTool

from utils.automation.Utils import get_clean_val


class FinalAnswer(BaseTool):
	name: str = "Tool to get the final answer"
	description: str = (
		'Use this tool when you are asked to the final answer'
		"'code_block': the compiled code from previous action, string type parameter"
	)

	def _run(self, code_block):
		code_block = get_clean_val(code_block)
		return {
			"action": "Final Answer",
			"action_input": code_block
		}
