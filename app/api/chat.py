from fastapi import APIRouter, HTTPException

from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse

from app.agents.orchestrator import AnalyticsAssistant

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

assistant = AnalyticsAssistant()


@router.post(
    "",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    try:

        answer = assistant.ask(
            request.question
        )

        return ChatResponse(

            success=True,

            question=request.question,

            answer=answer

        )

    except Exception as e:
        import traceback
        error_msg = traceback.format_exc()
        raise HTTPException(
            status_code=500,
            detail=error_msg
        )