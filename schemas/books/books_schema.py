from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str


class Book(BookBase):
    id: int
    is_available: bool = True


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookBorrow(BookBase):
    pass


class BookDelete(BookBase):
    pass
