from fastapi import APIRouter, HTTPException
from schemas.book import Book

books = []

router = APIRouter()

@router.get("/books")
def get_books():
    return books

@router.get("/books/{book_id}")
def get_prodcut(book_id: int):
    for book in books:
        if book_id == book["id"]:
            return book
        
    raise HTTPException(status_code=404, detail="book not found!")

@router.post("/books")
def create_book(book: Book):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "numb_pages": book.numb_pages,
        "category": book.category
    }

    books.append(new_book)
    return {
        "message": "book Created",
        "books": books
    }

@router.put("/books/{book_id}")
def update_book(book_id: int, upd_book: Book):
    for book in books:
        if book_id == book["id"]:
            book["title"] = upd_book.title
            book["author"] = upd_book.author
            book["numb_pages"] = upd_book.numb_pages
            book["category"] = upd_book.category

            return {
                "message": "book updated!",
                "book": book
            }
    raise HTTPException(status_code=404, detail="book not found!")

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book_id == book["id"]:
            books.remove(book)

            return {
                "message": "book deleted"
            }
    raise HTTPException(status_code=404, detail="book not found")