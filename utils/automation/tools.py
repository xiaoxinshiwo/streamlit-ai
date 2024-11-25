import ast


def get_clean_val(param_value, extracted_key='title'):
	if extracted_key in param_value:
		return param_value.get(extracted_key)
	else:
		return param_value


def extract_class_constructors(file_path):
	# Read the content of the Python file
	with open(file_path, 'r') as file:
		file_content = file.read()

	# Parse the content into an AST
	tree = ast.parse(file_content)

	# Extract all the classes and their names
	class_constructors = []
	for node in ast.walk(tree):
		if isinstance(node, ast.ClassDef):
			class_constructors.append(f"{node.name}()")

	return class_constructors


if __name__ == '__main__':
	# Example usage
	file_path = 'C:\\Users\\YonZhang\\PycharmProjects\\streamlit-ai\\utils\\automation\\lib\\requests.py'
	constructors = extract_class_constructors(file_path)
	for constructor in constructors:
		print(constructor, ',')
