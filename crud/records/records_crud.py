from datetime import date, datetime
from fastapi import HTTPException
from schemas.records.records_schema import BorrowRecord, BorrowRecordCreate
from crud.books.books_crud import BookCRUD
from crud.users.users_crud import UsersCRUD


borrow_records = []


class RecordsCRUD:
    @staticmethod
    def get_all_borrow_records():
        return borrow_records

    @staticmethod
    def get_borrow_record(record_id: int):
        for record in borrow_records:
            if record.id == record_id:
                return record
        raise HTTPException(status_code=404, detail="Borrow record not found")

    

    # @staticmethod
    # def get_records_by_user(user_id: int):
    #     user_records = [record for record in borrow_records
    #                     if record.user_id == user_id]
    #     if not user_records:
    #         raise HTTPException(status_code=404,
    #                             detail="No borrow records found for this user")
    #     return user_records
    @staticmethod
    def create_borrow_record(record: BorrowRecordCreate):
        new_record = BorrowRecord(
            id=len(borrow_records) + 1,
            user_id=record.user_id,
            book_id=record.book_id,
            borrow_date=record.borrow_date,
            return_date=None
            
        )
        borrow_records.append(new_record)
        return new_record

    @staticmethod
    def borrow_book(user_id: int, book_id: int, borrow_date: date,
                    return_date: date | None):

        # Validate User
        user = UsersCRUD.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.is_active:
            raise HTTPException(status_code=400, detail="User is not active")

        book = BookCRUD.get_book_by_id(book_id)

        # Validate Book
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        if not book.is_available:
            raise HTTPException(status_code=400,
                                detail="Book is not available")

        if RecordsCRUD.check_user_has_borrowed(user_id, book_id):
            raise HTTPException(status_code=400,
                                detail="User has already borrowed this book")

        # Mark book as unavailable
        book.is_available = False

        # create book record
        new_record = BorrowRecordCreate(
            user_id=user_id,
            book_id=book_id,
            borrow_date=borrow_date,
            return_date=return_date
        )

        return RecordsCRUD.create_borrow_record(new_record)

    @staticmethod
    def get_borrow_record_by_user(user_id: int):
        user_records = []
        for record in borrow_records:
            if record.user_id == user_id:
                user_records.append(record)
        return user_records

    @staticmethod
    def get_borrowed_book_by_user(user_id: int):
        user_records = [record for record in borrow_records
                        if record.user_id == user_id]
        if not user_records:
            raise HTTPException(status_code=404,
                                detail="No borrow records found for this user")
        return user_records

    @staticmethod
    def return_book(record_id: int):
        record = RecordsCRUD.get_borrow_record(record_id)
        if not record:
            raise HTTPException(status_code=404,
                                detail="Borrow record not found")

        if record.return_date is not None:
            raise HTTPException(status_code=400,
                                detail="Book has already been returned")

        record.return_date = datetime.now().date()

        # Mark book as available
        book = BookCRUD.get_book_by_id(record.book_id)
        if book:
            book.is_available = True

        # record = RecordsCRUD.get_borrow_record(record_id)
        return record


    @staticmethod
    def check_user_has_borrowed(user_id: int, book_id: int):
        for record in borrow_records:
            if record.user_id == user_id and record.book_id == book_id:
                return True
        return False


records_crud = RecordsCRUD()
