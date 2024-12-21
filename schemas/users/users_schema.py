from pydantic import BaseModel


class User_Base(BaseModel):
    name: str
    email: str


class User(User_Base):
    id: int
    is_active: bool = True


class User_Create(User_Base):
    pass


class User_Update(User_Base):
    pass


class User_Delete(User_Base):
    pass
