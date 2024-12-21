from fastapi import APIRouter, HTTPException
from schemas.books.books_schema import BookCreate, BookUpdate
from crud.books.books_crud import BookCRUD

books_router = APIRouter()


@books_router.get("/")
def get_books():
    return {"message": "successful", "data": BookCRUD.get_books()}


@books_router.get("/{book_id}")
def get_books_by_id(book_id: int):
    book = BookCRUD.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "successful", "data": book}


@books_router.post("/")
def create_new_book(payload: BookCreate):
    new_book = BookCRUD.create_new_book(payload)
    return {"message": "successfully created book!", "data": (new_book)}


@books_router.put("/{book_id}")
def update_book(book_id: int, payload: BookUpdate):
    expected_book = BookCRUD.get_book_by_id(book_id)
    if not expected_book:
        raise HTTPException(status_code=404, detail="Book not found")
    updated_book = BookCRUD.update_book(expected_book, payload)
    return {"message": "Success", "data": updated_book}


@books_router.put("/{book_id}/unavailable")
def mark_book_unavailable(book_id: int):
    return BookCRUD.mark_book_unavailable(book_id)


@books_router.post("/Borrow")
def borrow_book(book_id: int):
    return BookCRUD.borrow_book(book_id)


@books_router.put("/{book_id}/Borrow")
def return_book(book_id: int):
    return BookCRUD.return_book(book_id)


@books_router.delete("/{book_id}")
def delete_book(book_id: int):
    return BookCRUD.delete_book(book_id)
