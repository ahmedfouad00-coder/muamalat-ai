from app.prompts.rag_prompt import prompt
from app.rag.context_formatter import format_docs
from app.rag.retriever import retriever
from langchain_core.runnables import RunnablePassthrough,RunnableLambda
from app.rag.llm import llm

chain=(
    {"context":retriever|format_docs,
    "question":RunnablePassthrough()
    }
    |prompt
    |RunnableLambda(lambda x: x.to_string())
    |llm

)