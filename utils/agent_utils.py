import os

from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.utilities import PythonREPL
from langchain_openai import ChatOpenAI
from langsmith import Client

from utils.character_number_tool import CharacterNumber
from utils.email_util import EmailSender
from utils.word_number_tool import WordNumber


def get_strawberry_answer(question, memory, api_key):
	model = ChatOpenAI(api_key=api_key, model="gpt-4o-mini", temperature=0)
	tools = [CharacterNumber(), WordNumber()]
	client = Client(api_key=os.getenv(
		'LANGCHAIN_API_KEY'))  # LANGCHAIN_API_KEY=xxx, LANGCHAIN_TRACING_V2 = true https://docs.smith.langchain.com/
	prompt = client.pull_prompt("hwchase17/structured-chat-agent")

	agent = create_structured_chat_agent(
		llm=model,
		tools=tools,
		prompt=prompt
	)
	agent_executor = AgentExecutor.from_agent_and_tools(
		agent=agent, tools=tools, memory=memory, verbose=True, handle_parsing_errors=True
	)
	response = agent_executor.invoke({"input": question})
	print("response =====", response)
	return response


def python_executor(openai_api_key, prompt):
	agent_executor = create_python_agent(
		llm=ChatOpenAI(openai_api_key=openai_api_key, model="gpt-4o-mini", temperature=0),
		tool=PythonREPLTool(),
		verbose=True,
		agent_executor_kwargs={"handle_parsing_errors": True}
	)
	# print('agent_executor==',agent_executor)
	return agent_executor.invoke({"input": prompt})


def get_tool_collection_answer(question, memory, api_key):
	model = ChatOpenAI(api_key=api_key, model="gpt-4o-mini", temperature=0)
	tools = [
		CharacterNumber(),
		WordNumber(),
		EmailSender(),
		Tool(
			name='Python execution tool',
			description="When you request to deal with python code execution, you can use this tool",
			func=PythonREPL().run
		)
	]
	client = Client(api_key=os.getenv(
		'LANGCHAIN_API_KEY'))  # LANGCHAIN_API_KEY=xxx, LANGCHAIN_TRACING_V2 = true https://docs.smith.langchain.com/

	prompt = client.pull_prompt("hwchase17/structured-chat-agent")

	agent = create_structured_chat_agent(
		llm=model,
		tools=tools,
		prompt=prompt
	)
	agent_executor = AgentExecutor.from_agent_and_tools(
		agent=agent, tools=tools, memory=memory, verbose=True, handle_parsing_errors=True
	)
	response = agent_executor.invoke({"input": question})
	return response
