sessions={}
# getting sessions
def get_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = {
            "chat_history": [],
            "pending_question": None
        }

    return sessions[session_id]
#adding user message to chat history
def add_user_msg(session_id,message):
    session=get_session(session_id)
    session["chat_history"].append(
        {"role":"User",
        "content":message}
    )
#adding assistant message to chat history
def add_assistant_msg(session_id,message):
    session=get_session(session_id)
    session["chat_history"].append(
        {
            "role":"Assistant",
            "content":message
        }
    )

# retieving chat history
def get_chat_history(session_id):
    session=get_session(session_id)
    return "\n".join(
    f"{msg['role']}: {msg['content']}" for msg in session["chat_history"]
)

# clearing chat history
def clear_memory(session_id):
    session = get_session(session_id)
    session["chat_history"].clear()

# set pending question
def set_pending_question(session_id, question):
    session = get_session(session_id)
    session["pending_question"] = question

#get pending question
def get_pending_question(session_id):
    session = get_session(session_id)
    return session["pending_question"]

# clear pending question 
def clear_pending_question(session_id):
    session = get_session(session_id)
    session["pending_question"] = None
