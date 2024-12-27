"""Mongo models for the book collection."""

from beanie import Document


class Book(Document):
    """Basemodel for the book collection."""

    title: str
    authors: list[str]
    isbn: str
    genres: list[str]
    published_date: str
    summary: str

    class Settings:
        name = "books"

    class Config:
        schema_extra = {
            "example": {
                "title": "A book",
                "authors": ["Someone"],
                "isbn": "978-00-00-00-00-00",
                "genres": ["Fiction"],
                "published_date": "2019-01-10",
                "summary": "A book",
            }
        }
        name = "products"
