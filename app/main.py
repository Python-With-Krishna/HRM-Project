from fastapi import FastAPI

from app.api.routes.company import router as company_router

app = FastAPI(
    title="HRM API",
    version="1.0.0",
)


app.include_router(company_router)

@app.get("/")
def root():
    return {
        "message": "HRM API is running"
    }