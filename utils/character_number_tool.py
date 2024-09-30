from langchain.tools import BaseTool


class CharacterNumber(BaseTool):
	name: str = "Tool to calculate the number of times a character appears in a word"
	description: str = (
		"Use this tool when you are asked to count the number of characters in a word"
		"{'text':the given word, string type parameter}"
		"{'character':the given character, string type parameter}"
	)

	def _run(self, text, character):
		if character not in text:
			return 0
		count = 0
		for char in text:
			if char == character:
				count = count + 1
		return count  # try to change it to a wrong number
