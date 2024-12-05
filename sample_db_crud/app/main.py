from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, status as HTTPStatus

from api.endpoints import build_models

import uvicorn

app = FastAPI(docs_url="/docs")
app.include_router(build_models.local_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000
    )
