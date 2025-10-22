# agent_executor.py

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain import hub

from rag.retriever import get_top_k_chunks
from models.prompt_template import get_prompt_template

# Step 1: Define the search tool
def search_faq_tool(query: str, style: str = "default") -> str:
    docs = get_top_k_chunks(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt_fn = get_prompt_template(style)
    return prompt_fn.format(context=context, question=query)

search_tool = Tool(
    name="SearchFAQ",
    func=search_faq_tool,
    description="Useful for answering user questions about product or company policies using the FAQ context. Input should be a user question."
)

# Step 2: Setup LangChain Agent with tools and functions
llm = ChatOpenAI(temperature=0.0)
prompt = hub.pull("hwchase17/openai-functions-agent") 
agent = create_openai_functions_agent(llm=llm, tools=[search_tool], prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=[search_tool], verbose=True)

# Step 3: Main run method for incoming queries
def run_agent(query: str) -> dict:
    result = agent_executor.invoke({"input": query}, config=RunnableConfig())
    return {
        "query": query,
        "answer": result["output"]
    }

print("✅ LangChain Agent loaded with tools:")
for tool in [search_tool]:
    print(f"🔧 {tool.name}: {tool.description}")