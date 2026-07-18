from app.prompts.agent_prompts.rephraser_prompt import rephraser_prompt
from app.rag.llm import llm

rephraser_chain= rephraser_prompt | llm

#building the rephraser agent function
def rephraser_agent(chat_history,question):
    response=rephraser_chain.invoke(
        {"chat_history":chat_history,
        "question":question}
    )
    return response.content.strip()