from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from database.db import create_table, engine
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_table()
    print("Database tables verfied.")

    yield 

    await engine.dispose()
    print("Database connection pool closed.")


app = FastAPI(
    title="Student Result Portal for research Pourpose",
    lifespan=lifespan
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)