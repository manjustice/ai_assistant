from fastapi import HTTPException
from fastapi import APIRouter, Request
from starlette import status

from app.config import templates
from app.utils.answer import find_answer


router = APIRouter()


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/")
def get_answer(data: dict):
    question = data.get("question")

    if question is not None:
        answer = find_answer(question)
        return {"question": data["question"], "answer": answer}

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="To get answer you should write question"
    )
