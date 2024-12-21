from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class BorrowRecordBase(BaseModel):
    book_id: int
    user_id: int
    borrow_date: date = Field(default_factory=date.today)
    return_date: Optional[date] = None

    # class Config:
    #     orm_mode = True


class BorrowRecordCreate(BaseModel):
    book_id: int
    user_id: int
    borrow_date: date = Field(default_factory=date.today)


class BorrowRecord(BorrowRecordBase):
    id: int


