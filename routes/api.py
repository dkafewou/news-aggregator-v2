from fastapi import APIRouter
from src.endpoints import news

router = APIRouter()
router.include_router(news.router)
