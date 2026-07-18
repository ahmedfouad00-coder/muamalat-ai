from app.Agents.clarification_agent import clarification_agent
from app.Agents.rephraser_agent import rephraser_agent
from app.Agents.memory import get_chat_history,set_pending_question,get_pending_question, clear_pending_question,add_assistant_msg,add_user_msg
from app.rag.chain import chain
# merging question
def merge_question(original_question: str, clarification_answer: str):
    replacements = [
        "ذلك",
        "هذا",
        "هذه",
        "حكمه",
        "المذكور",
        "السابق"
    ]

    question = original_question
    
    for word in replacements:
        if word in question:
            question = question.replace(word, clarification_answer)
            return question

    return clarification_answer

# processing the user question
def process_question(session_id:str,question : str):
    original_question=question
    history=get_chat_history(session_id)
    pending = get_pending_question(session_id)
    if pending:
        question=merge_question(pending,question)
        
        clear_pending_question(session_id)
    clarification=clarification_agent(history,question)
    
    #check if clarification needed
    if not clarification["is_clear"]:
        add_user_msg(session_id, original_question)
        set_pending_question(session_id, question)
        add_assistant_msg(session_id, clarification["clarification_question"])
        return clarification["clarification_question"]

    # if no clarification needed, reohrase the question
    new_question=rephraser_agent(history,question)

    #RAG chain
    answer=chain.invoke(new_question)
    add_user_msg(session_id,original_question)
    add_assistant_msg(session_id,answer.content)
    return {
        "Assistant":answer.content
    }



