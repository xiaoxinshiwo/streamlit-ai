from langchain_core.tools import BaseTool

from utils.automation.base_lib_class import BaseLibClass
from utils.automation.tools import get_clean_val


class ClickButton(BaseTool):
	name: str = "Tool to click a button"
	description: str = (
		'Use this tool when you are asked to click a button'
		"{'selector': the identity to locate an element, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, selector):
		selector = get_clean_val(selector)
		return f"await page.click('{selector}');"


class SelectDropdownOption(BaseTool):
	name: str = "Tool to select a dropdown option"
	description: str = (
		'Use this tool when you are asked to to select a dropdown option'
		"{'selector': the identity to locate a dropdown, string type parameter}"
		"{'value': the value of a option to be selected, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, selector, value):
		selector = get_clean_val(selector)
		value = get_clean_val(value)
		return f"await Ctrls.selectDropdownOption(page,'{selector}','{value}' );"


class SelectRadio(BaseTool):
	name: str = "Tool to click a radio button"
	description: str = (
		'Use this tool when you are asked to to click a radio button'
		"{'selector': the identity to locate a dropdown, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, selector):
		selector = get_clean_val(selector)
		return f"await page.click('{selector}');"


class FillInput(BaseTool):
	name: str = "Tool to fill value into text box"
	description: str = (
		'Use this tool when you are asked to fill value into text box'
		"{'selector': the identity to locate a text box, string type parameter}"
		"{'value': value of a text box, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, selector, value):
		selector = get_clean_val(selector)
		value = get_clean_val(value)
		return f"await page.fill('{selector}', '{value}');"


class SelectSingleAcl(BaseTool):
	name: str = "Tool to select a single ACL"
	description: str = (
		'Use this tool when you are asked to select a single ACL'
		"{'selector': the identity to locate a single ACL, string type parameter}"
		"{'value': value of single ACL, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, selector, value):
		selector = get_clean_val(selector)
		value = get_clean_val(value)
		return f"await Ctrls.selectSingleAcl(page, '{selector}', '{value}');"


class Ctrls(BaseLibClass):
	@staticmethod
	def get_tools():
		return [
			ClickButton(),
			SelectDropdownOption(),
			SelectRadio(),
			FillInput(),
			SelectSingleAcl(), ]
