"""App for the book creator."""

import fastapi
import uvicorn

from pants_poc.db.books_model import Book
from utils.common import wrapper


APP = fastapi.FastAPI(
    title="Book Creator",
    version="0.0.1",
    description="Create a book entry in the database",
    lifespan=wrapper(db_model=Book),
)


@APP.post("/books/")
async def create_item(book: Book):
    """Create a book"""
    await book.save()
    return {"message": "Book created successfully"}



def start_service() -> None:
    """Run the service."""
    uvicorn.run(APP, host='0.0.0.0', port=8000)


if __name__ == "__main__":
    start_service()