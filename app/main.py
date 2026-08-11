from fastapi import FastAPI

from app.api.routes.user import router as users_router


app = FastAPI(
    title="HRM API",
    version="1.0.0",
)


app.include_router(users_router)


@app.get("/")
def root():
    return {
        "message": "HRM API is running"
    }