from fastapi import FastAPI
from app.api.api_v1 import api_router
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://0.0.0.0:8000"
]

def create_app() -> FastAPI:
    app = FastAPI(debug=True)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api/v1")
    return app