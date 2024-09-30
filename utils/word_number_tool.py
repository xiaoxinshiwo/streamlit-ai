import re

from langchain.tools import BaseTool


class WordNumber(BaseTool):
	name: str = "Tool to count how many words appear in a sentence"
	"""
	 If the parameter type is not described, parameters in the following format may be entered when passing parameters, causing execution exceptions.
	{
		"action": "Tool to count how many words appear in a sentence",
		"action_input": {
			"text": {
				"title": "山重水复疑无路，柳暗花明又一村"
			}
		}
	}
	"""
	description: str = (
		"Use this tool when you are asked to count the number of word in a sentence"
		"{'text':the given sentence, string type parameter}"
	)

	def _run(self, text):
		print("text==", text)
		# characters
		english_words = re.findall(r'[a-zA-Z]+', text)
		word_count = len(english_words)

		# chinese
		chinese_characters = re.findall(r'[\u4e00-\u9fff]', text)
		char_count = len(chinese_characters)

		return word_count + char_count


if __name__ == '__main__':
	w = WordNumber()
	w.run(' hello, 我来自中国')
