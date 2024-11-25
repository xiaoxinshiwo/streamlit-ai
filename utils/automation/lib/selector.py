from langchain_core.tools import BaseTool

from utils.automation.base_lib_class import BaseLibClass
from utils.automation.tools import get_clean_val


class ByName(BaseTool):
	name: str = "Tool to generate code for selector by name"
	description: str = (
		"Use this tool to generate a selector by tag and name attribute."
		" {'tag': the HTML tag, string type parameter}"
		" {'name': the name attribute, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, tag, name):
		tag = get_clean_val(tag)
		name = get_clean_val(name)
		return f"Selector.byName('{tag}','{name}');"


class ByPartialClass(BaseTool):
	name: str = "Tool to generate code for selector by partial class"
	description: str = (
		"Use this tool to generate a selector by tag and partial class."
		" {'tag': the HTML tag, string type parameter}"
		" {'clz': the partial class name, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, tag, clz):
		tag = get_clean_val(tag)
		clz = get_clean_val(clz)
		return f"Selector.byPartialClass('{tag}','{clz}');"


class ByPartialAttribute(BaseTool):
	name: str = "Tool to generate code for selector by partial attribute"
	description: str = (
		"Use this tool to generate a selector by tag and partial attribute."
		" {'tag': the HTML tag, string type parameter}"
		" {'attributName': the attribute name, string type parameter}"
		" {'attributeValue': the partial value of the attribute, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, tag, attributName, attributeValue):
		tag = get_clean_val(tag)
		attributName = get_clean_val(attributName)
		attributeValue = get_clean_val(attributeValue)
		return f"Selector.byPartialAttribute('{tag}','{attributName}', '{attributeValue}');"


class ByPartialAttributes(BaseTool):
	name: str = "Tool to generate code for selector by multiple partial attributes"
	description: str = (
		"Use this tool to generate a selector by tag and multiple partial attribute values."
		" {'tag': the HTML tag, string type parameter}"
		" {'attributName': the attribute name, string type parameter}"
		" {'attributeValues': a list of partial attribute values, array type parameter}"
	)
	return_direct: bool = True

	def _run(self, tag, attributName, attributeValues):
		tag = get_clean_val(tag)
		attributName = get_clean_val(attributName)
		attributeValues = get_clean_val(attributeValues)
		return f"Selector.byPartialText(('{tag}', '{attributName}', {attributeValues});"


class ByPartialText(BaseTool):
	name: str = "Tool to generate code for selector by partial text"
	description: str = (
		"Use this tool to generate a selector by tag and partial text."
		" {'tag': the HTML tag, string type parameter}"
		" {'text': the partial text, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, tag, text):
		tag = get_clean_val(tag)
		text = get_clean_val(text)
		return f"Selector.byPartialText(('{tag}', '{text}');"


class ByPartialTexts(BaseTool):
	name: str = "Tool to generate code for selector by multiple partial texts"
	description: str = (
		"Use this tool to generate a selector by tag and multiple partial texts."
		" {'tag': the HTML tag, string type parameter}"
		" {'texts': a list of partial texts, array type parameter}"
	)
	return_direct: bool = True

	def _run(self, tag, texts):
		tag = get_clean_val(tag)
		texts = get_clean_val(texts)

		return f"Selector.byPartialTexts(('{tag}', {texts});"


class ByFullText(BaseTool):
	name: str = "Tool to generate code for selector by full text"
	description: str = (
		"Use this tool to generate a selector by tag and exact text."
		" {'tag': the HTML tag, string type parameter}"
		" {'text': the exact text, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, tag, text):
		tag = get_clean_val(tag)
		text = get_clean_val(text)
		return f"Selector.byFullText('{tag}', '{text}');"


class ByFullAttribute(BaseTool):
	name: str = "Tool to generate code for selector by full attribute"
	description: str = (
		"Use this tool to generate a selector by tag and exact attribute."
		" {'tag': the HTML tag, string type parameter}"
		" {'attributeName': the attribute name, string type parameter}"
		" {'attributeValue': the exact value of the attribute, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, tag, attributeName, attributeValue):
		tag = get_clean_val(tag)
		attributeName = get_clean_val(attributeName)
		attributeValue = get_clean_val(attributeValue)
		return f"Selector.byFullAttribute('{tag}','{attributeName}', '{attributeValue}');"


class ByHref(BaseTool):
	name: str = "Tool to generate code for selector by href"
	description: str = (
		"Use this tool to generate a selector by href attribute."
		" {'href': the href value, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, href):
		href = get_clean_val(href)
		return f"Selector.byHref('{href}');"


class ByLast(BaseTool):
	name: str = "Tool to generate code for selector by last element"
	description: str = (
		"Use this tool to generate a selector for the last element of a given selector."
		" {'selector': the base selector, string type parameter}"
	)
	return_direct: bool = True

	def _run(self, selector):
		selector = get_clean_val(selector)
		return f"Selector.byLast('{selector}');"


class Selector(BaseLibClass):
	@staticmethod
	def get_tools():
		return [
			ByName(),
			ByPartialClass(),
			ByPartialAttribute(),
			ByPartialAttributes(),
			ByPartialText(),
			ByPartialTexts(),
			ByFullText(),
			ByFullAttribute(),
			ByHref(),
			ByLast(),
		]
