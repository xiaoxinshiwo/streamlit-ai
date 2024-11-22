from langchain_core.tools import BaseTool

from utils.automation.tools import get_clean_val


class SaveRequest(BaseTool):
	name: str = "Tool to generate code to save a lib"
	description: str = (
		'Use this tool when you are asked to save a lib, need to import dependency: import {Requests} from "@lib/Requests";'
	)

	def _run(self):
		return "await Requests.saveRequest(page);"


class SubmitRequest(BaseTool):
	name: str = "Tool to generate code to submit a lib"
	description: str = (
		'Use this tool when you are asked to submit a lib, need to import dependency: import {Requests} from "@lib/Requests";'
	)

	def _run(self):
		return "await Requests.submitRequest(page);"


class CreateRequest(BaseTool):
	name: str = "Tool to generate code to c creates a lib of a specific type"
	description: str = (
		'Use this tool when you are asked to save a lib  of a specific type, need to import dependency: import {Requests} from "@lib/Requests";'
		"'request_type': the type of a lib, string type parameter"
	)

	def _run(self, request_type):
		request_type = get_clean_val(request_type)
		return f'await Requests.openCreateRequestPage(page, "{request_type}");'


class DeleteRequest(BaseTool):
	name: str = "Tool to generate code to delete a lib"
	description: str = (
		'Use this tool when you are asked to delete a lib, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'request_id': the id of a lib, number type parameter}"
	)

	def _run(self, request_id):
		request_id = get_clean_val(request_id)
		return f"await Requests.deleteRequest(page, {request_id});"


class AddNote(BaseTool):
	name: str = "Tool to generate code to add note to a lib"
	description: str = (
		'Use this tool when you are asked to add note to a lib, need to import dependency: import {Requests} from "@lib/Requests";'
		"'note': the content, string type parameter"
	)

	def _run(self, note):
		note = get_clean_val(note)
		return f"await Requests.addNote(page, '{note}');"


class ClickWorkflowAction(BaseTool):
	name: str = "Tool to generate code to click workflow button"
	description: str = (
		'Use this tool when you are asked to click workflow button, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'action':  the name of workflow button, string type parameter}"
	)

	def _run(self, action):
		action = get_clean_val(action)
		return f"await Requests.clickWfAction(page, '{action}');"


class ClickButton(BaseTool):
	name: str = "Tool to generate code to click a button"
	description: str = (
		"Use this tool when you are asked to click a button"
		"{'selector': the identity to locate an element, string type parameter}"
	)

	def _run(self, selector):
		selector = get_clean_val(selector)
		return f'await page.click("{selector}");'


class SelectDropdownOption(BaseTool):
	name: str = "Tool to generate code to select a dropdown option"
	description: str = (
		'Use this tool when you are asked to to select a dropdown option,need to import dependency: import {Ctrls} from "@lib/Ctrls";'
		"'selector': the identity to locate a dropdown, string type parameter"
		"'value': the value of a option to be selected, string type parameter"
	)

	def _run(self, selector, value):
		selector = get_clean_val(selector)
		value = get_clean_val(selector)
		return f'await Ctrls.selectDropdownOption(page,{selector},{value} );'


class SelectRadio(BaseTool):
	name: str = "Tool to generate code to click a radio button"
	description: str = (
		'Use this tool when you are asked to to click a radio button'
		"'selector': the identity to locate a dropdown, string type parameter"
	)

	def _run(self, selector):
		selector = get_clean_val(selector)
		return f'await page.click("{selector}");'


class FillInput(BaseTool):
	name: str = "Tool to generate code to fill value into text box"
	description: str = (
		'Use this tool when you are asked to fill value into text box'
		"'selector': the identity to locate a text box, string type parameter"
		"'value': value of a text box, string type parameter"
	)

	def _run(self, selector, value):
		selector = get_clean_val(selector)
		value = get_clean_val(value)
		return f'await page.fill("{selector}", "{value}");'


class SelectSingleAcl(BaseTool):
	name: str = "Tool to generate code to select a single ACL"
	description: str = (
		'Use this tool when you are asked to select a single ACL'
		"'selector': the identity to locate a single ACL, string type parameter"
		"'value': value of single ACL, string type parameter"
	)

	def _run(self, selector, value):
		selector = get_clean_val(selector)
		value = get_clean_val(value)
		return f'await Ctrls.selectSingleAcl(page, "{selector}", "{value}");'


class DeleteRequestOnRequestDetailPage(BaseTool):
	name: str = "Tool to generate code to delete request on request detail page"
	description: str = (
		'Use this tool when you are asked to delete request on request detail page, need to import dependency: import {Requests} from "@lib/Requests";'
	)

	def _run(sel):
		return "await Requests.deleteRequestOnRequestDetailPage(page);"


class Requests():
	@staticmethod
	def get_tools():
		return [
			SaveRequest(),
			SubmitRequest(),
			CreateRequest(),
			DeleteRequest(),
			AddNote(),
			ClickWorkflowAction(),
			ClickButton(),
			SelectDropdownOption(),
			SelectRadio(),
			FillInput(),
			SelectSingleAcl(),
			DeleteRequestOnRequestDetailPage(),
		]
