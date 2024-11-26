from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool
from langchain_openai import ChatOpenAI

from utils import agent_prompts
from utils.character_number_tool import CharacterNumber
from utils.word_number_tool import WordNumber


def get_strawberry_answer(question, memory, api_key):
	model = ChatOpenAI(api_key=api_key, model="gpt-4o-mini", temperature=0)
	tools = [CharacterNumber(), WordNumber()]
	prompt = agent_prompts.structured_chat_agent

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


def python_executor(question, api_key):
	model = ChatOpenAI(api_key=api_key, model="gpt-4o-mini", temperature=0)
	agent_executor = create_python_agent(
		llm=model,
		tool=PythonREPLTool(),
		verbose=True,
		agent_executor_kwargs={"handle_parsing_errors": True}
	)
	response = agent_executor.invoke({"input": question})
	return response
