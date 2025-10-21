from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
# Removed unused AgentExecutor and create_react_agent
from utils.config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE
from rag.retriever import get_top_k_chunks
from models.prompt_template import get_prompt_template

def search_faq_tool(query: str, style: str = "default") -> str:
    docs = get_top_k_chunks(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt_fn = get_prompt_template(style)
    return prompt_fn.format(context=context, question=query)

def answer_with_agent(query: str, style: str = "default") -> dict:
    chunks: list[Document] = get_top_k_chunks(query)

    # Combine document chunks into context string
    context = "\n\n".join([doc.page_content for doc in chunks])
    sources = [{"source": doc.metadata.get("source", "unknown"), "content": doc.page_content} for doc in chunks]

    # Build prompt
    prompt_template = get_prompt_template(style)
    prompt = prompt_template.format(context=context, question=query)

    # Call LLM
    llm = ChatOpenAI()
    response = llm.invoke(prompt)

    return {
        "query": query,
        "answer": response.content,
        "sources": sources
    }