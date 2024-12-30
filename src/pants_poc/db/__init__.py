"""Package for interacting with mongo."""

import os
from typing import Type

from beanie import Document, init_beanie
import motor


async def init_db(db_model: Type[Document]):
    """Initialize the database."""
    db_host = os.getenv("MONGO_HOST", "localhost")
    client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{db_host}:27017")
    await init_beanie(database=client.db_name, document_models=[db_model])
