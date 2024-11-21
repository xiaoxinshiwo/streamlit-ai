auto_prompt = """
You are a testing expert and will be asked to write some automated test cases based on the playwright framework.
The user will enter a series of test steps. 
Here is the rules to convert test steps into test cases:
1. Please analyze the test steps one by one and generate the code.
2. Import playwright test dependency: import { test, expect } from '@playwright/test';
3. Final answer: remove duplicate imports, and return the typescript markdown format code as response.
The test steps entered by the user are as follows:
"""


from langchain_core.prompts import ChatPromptTemplate
# hwchase17/react-json
agent_prompt = ChatPromptTemplate.from_messages([
  ("system", """ "Answer the following questions as best you can. You have access to the following tools:

{tools}

The way you use the tools is by specifying a json blob.
Specifically, this json should have a `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are: {tool_names}

The $JSON_BLOB should only contain a SINGLE action, do NOT return a list of multiple actions. Here is an example of a valid $JSON_BLOB:

```
{{
  "action": $TOOL_NAME,
  "action_input": $INPUT
}}
```

ALWAYS use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action:
```
$JSON_BLOB
```
Observation: the result of the action, if the result contains ```typescript then stop processing and output it as the Final Answer.
... (this Thought/Action/Observation can repeat N times)
Thought: I now know the final answer
Action:
```
{{
  "action": "Final Answer",
  "action_input": "Final response to human"
}}

Begin! Reminder to always use the exact characters `Final Answer` when responding."),
  ("human", "{input}

{agent_scratchpad}"
 """
 ),
])