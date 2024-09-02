from app.api.routes import create_app
from app.models.database import engine, Base
from .exceptions import custom_http_exception_handler
from .exceptions import custom_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi import Request, HTTPException



app = create_app()

app.add_exception_handler(HTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, custom_validation_exception_handler)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()
