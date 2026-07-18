from fastapi import APIRouter
from app.api.schemas import ChatRequest,ChatResponse
from app.pipeline import process_question

router=APIRouter()

@router.post("/chat",response_model=ChatResponse)

# chat function
def chat(request:ChatRequest):
    result=process_question(
        session_id=request.session_id,
        question=request.question
        )

    if isinstance(result,str):
        return ChatResponse(answer=result)
    return ChatResponse(answer=result["Assistant"])