import json

from langchain.agents import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

'''
example:
假定现在退休年龄时男64， 女59， 如果缴纳的社保17年后才能回本，请问能够回本的人数男女各是多少，退休人数男女各是多少，请绘制柱状图
'''

PROMPT_TEMPLATE = """
You are a data analysis assistant, and your responses depend on the user's request.

1. For text-based questions, answer in the following format:
   {"answer": "<your answer here>"}
For example:
   {"answer": "The product with the highest order volume is 'MNWC3-067'"}

2. If the user requires a table, answer in the following format:
   {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}

3. If the user's request is suitable for a bar chart, answer in the following format:
   {"bar": {"columns": ["A", "B", "C", ...], "data": [34, 21, 91, ...]}}

4. If the user's request is suitable for a line chart, answer in the following format:
   {"line": {"columns": ["A", "B", "C", ...], "data": [34, 21, 91, ...]}}

5. If the user's request is suitable for a scatter plot, answer in the following format:
   {"scatter": {"columns": ["A", "B", "C", ...], "data": [34, 21, 91, ...]}}
Note: We only support three types of charts: "bar", "line", and "scatter".

Please return all outputs as JSON strings. Ensure that all strings in the "columns" list and data list are enclosed in double quotes.
For example: {"columns": ["Products", "Orders"], "data": [["32085Lip", 245], ["76439Eye", 178]]}

The user request you need to handle is as follows: 

"""


def dataframe_agent(openai_api_key, df, query):
	model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key, temperature=0)
	agent = create_pandas_dataframe_agent(llm=model,
										  agent_type=AgentType.OPENAI_FUNCTIONS,
										  allow_dangerous_code=True,
										  df=df,
										  agent_executor_kwargs={"handle_parsing_errors": True},
										  verbose=True
										  )
	prompt = PROMPT_TEMPLATE + query
	response = agent.invoke({"input": prompt})
	response_dict = json.loads(response["output"])
	return response_dict
