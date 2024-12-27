"""App for the book reader."""

import fastapi
from utils.common import wrapper
import uvicorn

from pants_poc.db.books_model import Book

APP = fastapi.FastAPI(
    title="Book Creator",
    version="0.0.1",
    description="Create a book entry in the database",
    lifespan=wrapper(db_model=Book),
)


@APP.get("/books/")
async def read_books() -> list[Book]:
    result = await Book.find_all().to_list()
    return result


def start_service() -> None:
    """Run the service."""
    uvicorn.run(APP, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start_service()
