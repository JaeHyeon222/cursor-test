from fastapi import APIRouter
from .endpoints import image

api_router = APIRouter()
api_router.include_router(image.router, prefix="/image", tags=["image"]) 