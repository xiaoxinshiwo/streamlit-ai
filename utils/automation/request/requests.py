from langchain_core.tools import BaseTool


class Login(BaseTool):
	name: str = "Tool to generate code to login"
	description: str = (
		"Use this tool when you are asked to login"
	)

	def _run(self):
		return 'await login(page, PPMURL,"admin","admin");'


class SaveRequest(BaseTool):
	name: str = "Tool to generate code to save a request"
	description: str = (
		"Use this tool when you are asked to save a request"
	)

	def _run(self):
		return "await Requests.saveRequest(page);"


class CreateRequest(BaseTool):
	name: str = "Tool to generate code to c creates a request of a specific type"
	description: str = (
		"Use this tool when you are asked to save a request  of a specific type"
		"{request_type: the type of a request, string type parameter}"
	)

	def _run(self, request_type):
		return f'await Requests.openCreateRequestPage(page, "{request_type}");'


class DeleteRequest(BaseTool):
	name: str = "Tool to generate code to delete a request"
	description: str = (
		"Use this tool when you are asked to delete a request"
		"{request_id: the id of a request, number type parameter}"
	)

	def _run(self, request_id):
		return f"await Requests.deleteRequest(page, {request_id});"


class AddNote(BaseTool):
	name: str = "Tool to generate code to add note to a request"
	description: str = (
		"Use this tool when you are asked to add note to a request"
		"{note: the content, string type parameter}"
	)

	def _run(self, note):
		return f"await Requests.addNote(page, '{note}');"


class ClickWorkflowAction(BaseTool):
	name: str = "Tool to generate code to click workflow button"
	description: str = (
		"Use this tool when you are asked to click workflow button"
		"{action:  the name of workflow button, string type parameter}"
	)

	def _run(self, action):
		return f"await Requests.clickWfAction(page, '{action}');"


class ClickButton(BaseTool):
	name: str = "Tool to generate code to click a button"
	description: str = (
		"Use this tool when you are asked to click a button"
		"{selector: the identity to locate an element, string type parameter}"
	)

	def _run(self, selector):
		return f'await page.click("{selector}");'
