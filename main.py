from fastapi import FastAPI
from routers.books.books_router import books_router
from routers.users.users_router import users_router
from routers.records.records_router import records_router


app = FastAPI()


app.include_router(books_router, prefix="/books", tags=["Books"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(records_router, prefix="/records", tags=["Records"])


@app.get("/")
def Home():
    return {"message": "welcome home"}
