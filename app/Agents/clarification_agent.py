import json
from app.prompts.agent_prompts.clarification_prompt import clarification_prompt
from app.rag.llm import llm

clarification_chain= clarification_prompt | llm

#building the clarification agent function
def clarification_agent(chat_history,question):
    response=clarification_chain.invoke(
        {"chat_history": chat_history,
        "question": question}
    )

    result=(response.content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )
    return json.loads(result)

