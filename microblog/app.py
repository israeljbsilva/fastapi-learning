from fastapi import FastAPI

from .routes import main_router


app = FastAPI(
    title="Microblog",
    version="0.1.0",
    description="Microblog is a posting app",
)
app.include_router(main_router)


@app.get("/")
async def index():
    return {"hello": "world"}

