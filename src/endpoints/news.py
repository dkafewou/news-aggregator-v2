from fastapi import APIRouter
from src.utils import service
from typing import Optional

# APIRouter creates list and search operations for news
router = APIRouter(
    prefix="/news",
    tags=["News"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_news(q: Optional[str] = ""):
    news = await service.get_news(q)

    return news
