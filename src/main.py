from fastapi import FastAPI

from src.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Blog API backend",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify API is running.
    """
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
