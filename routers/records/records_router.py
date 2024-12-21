from datetime import date
from fastapi import APIRouter
from crud.records.records_crud import RecordsCRUD, BorrowRecord
from schemas.records.records_schema import BorrowRecordCreate, BorrowRecord

records_router = APIRouter()


@records_router.get("/records", response_model=list[BorrowRecord])
async def get_all_borrow_records():
    return RecordsCRUD.get_all_borrow_records()


@records_router.get("/records/{record_id}", response_model=BorrowRecord)
async def get_borrow_record(record_id: int):
    return RecordsCRUD.get_borrow_record(record_id)


@records_router.post("/records", response_model=BorrowRecordCreate)
async def create_borrow_record(record: BorrowRecordCreate):
    return RecordsCRUD.create_borrow_record(record)


# @records_router.get("/record/{user_id}")
# async def get_borrow_record_by_User(user_id):
#     return RecordsCRUD.get_borrow_record_by_user(user_id)

# @records_router.get("/records/user/{user_id}",
#                     response_model=list[BorrowRecord])
# async def get_records_by_user(user_id: int):
#     return RecordsCRUD.get_records_by_user(user_id)
# @records_router.get("/borrow")
# async def borrow_book(user_id: int, book_id: int):
#     return RecordsCRUD.borrow_book()

@records_router.post("/borrow", response_model=BorrowRecordCreate)
async def borrow_book(user_id: int, book_id: int,
                      borrow_date: date,
                      return_date: date | None):
    return RecordsCRUD.borrow_book(user_id, book_id, borrow_date, return_date)


@records_router.get("/records/user/{user_id}")
async def get_borrowed_book_by_user(user_id: int,
                                    response_model=list[BorrowRecord]):
    return RecordsCRUD.get_borrowed_book_by_user(user_id)


@records_router.get("/records/users/{user_id}")
async def get_borrow_record_by_user(user_id: int):
    return RecordsCRUD.get_borrow_record_by_user(user_id)


@records_router.put("/borrow/{record_id}/return", response_model=BorrowRecord)
async def return_book(record_id: int):
    return RecordsCRUD.return_book(record_id)


