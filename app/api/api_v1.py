from fastapi import APIRouter
from app.views import user_views

api_router = APIRouter()

api_router.include_router(user_views.router, prefix="/users", tags=["users"])
