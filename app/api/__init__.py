from fastapi import APIRouter

from .assistant import router as assistant_router


api_router = APIRouter()

api_router.include_router(assistant_router, prefix="", tags=["Assistant"])
