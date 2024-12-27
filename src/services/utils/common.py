"""Common functions to use."""

import contextlib

import beanie
import fastapi

from pants_poc.db import init_db


def wrapper(db_model: beanie.Document) -> callable:
    @contextlib.asynccontextmanager
    async def lifespan(_: fastapi.FastAPI):
        """Define what happens before and after service start."""
        print("Initializing database...")
        await init_db(db_model=db_model)
        print("Database initialized...")
        yield

    return lifespan
