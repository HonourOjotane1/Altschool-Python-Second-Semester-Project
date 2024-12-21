from fastapi import HTTPException
from schemas.books.books_schema import Book, BookCreate, BookUpdate


books = [
    Book(title="book1", author="author1", id=1, is_available=True),
    Book(title="book2", author="author2", id=2, is_available=True)
]


class BookCRUD:
    @staticmethod
    def get_books():
        return books

    @staticmethod
    def get_book_by_id(book_id: int):
        Book | None
        for current_book in books:
            if current_book.id == book_id:
                return current_book
        return None

    @staticmethod
    def create_new_book(book: BookCreate):
        new_book = Book(
            id=len(books)+1,
            title=book.title,
            author=book.author,
            is_available=True)
        books.append(new_book)
        return new_book

    @staticmethod
    def update_book(book: Book, data: BookUpdate):
        if not Book:
            raise HTTPException(status_code=404, detail="Book not found")
        book.title = data.title
        book.author = data.author
        return book

    @staticmethod
    def mark_book_unavailable(book_id):
        book = BookCRUD.get_book_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        book.is_available = False
        return book

    @staticmethod
    def delete_book(book_id: int):
        for index, book in enumerate(books):
            if book.id == book_id:
                del books[index]
                return {"message": "Book deleted successfully"}
        raise HTTPException(status_code=404, detail="Book not found")

    @staticmethod
    def borrow_book(book_id: int):
        book = BookCRUD.get_book_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        if not book.is_available:
            raise HTTPException(status_code=400,
                                detail="Book is not available")
        book.is_available = False
        return book

    @staticmethod
    def return_book(book_id: int):
        book = BookCRUD.get_book_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        if book.is_available:
            raise HTTPException(status_code=400,
                                detail="Book is already available")
        book.is_available = True
        return book


books_crud = BookCRUD()
