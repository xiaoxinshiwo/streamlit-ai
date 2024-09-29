from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def read_uploaded_and_split_pdf(uploaded_file):
	file_content = uploaded_file.read()
	temp_file_path = "temp.pdf"
	with open(temp_file_path, "wb") as temp_file:
		temp_file.write(file_content)
	loader = PyPDFLoader(temp_file_path)
	docs = loader.load()
	text_splitter = RecursiveCharacterTextSplitter(
		chunk_size=1000,
		chunk_overlap=50,
		separators=["\n", "。", "！", "？", "，", "、", ""]
	)
	return text_splitter.split_documents(docs)
