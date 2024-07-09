from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date, timedelta

app = FastAPI()


class Book(BaseModel):
    isbn: str
    title: str
    author: str
    genre: str
    language: str
    status: str


class Library:
    def __init__(self):
        self.books = {
            'Percy Jackson and the Lightning Thief': Book(isbn='0-1781-0776-X',
                                                          title='Percy Jackson and the Lightning Thief',
                                                          author='Rick Riordan', genre='Fantasy', language='English',
                                                          status='Available'),
            'Percy Jackson and the Sea of Monsters': Book(isbn='0-8251-8267-0',
                                                          title='Percy Jackson and the Sea of Monsters',
                                                          author='Rick Riordan', genre='Fantasy', language='English',
                                                          status='Available')
        }

    def add_book(self, book: Book):
        if book.title in self.books:
            raise HTTPException(status_code=400, detail="Book already exists in the library")
        self.books[book.title] = book
        return book.title, "has been added to the library"

    def delete_book(self, title: str):
        if title not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        del self.books[title]
        return {"message": f"{title} has been deleted from the library"}

    def search_book(self, title: str):
        if title not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        return self.books[title]

    def update_book_status(self, title: str, status: str):
        if title not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        self.books[title].status = status
        return {"message": f"The status of {title} has been updated"}

    def view_library(self):
        return {"books": list(self.books.values())}

    def view_book_details(self, title: str):
        if title not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        return self.books[title]

    def issue_book(self, title: str, student_name: str, student_id: str):
        if title not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        if self.books[title].status != "Available":
            raise HTTPException(status_code=400, detail="Book is currently unavailable")
        self.books[title].status = f"Issued to {student_id}"
        return {
            "message": f"{title} has been issued to {student_name} ({student_id}) on {date.today()}",
            "return_date": date.today() + timedelta(days=15)
        }


library = Library()


@app.post("/admin/login")
async def admin_login(username: str, password: str):
    if username == "Admin" and password == "12345678":
        return {"message": "Admin login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@app.post("/books/{title}/issue")
async def issue_book(title: str, student_name: str, student_id: str):
    return library.issue_book(title, student_name, student_id)


@app.get("/books/{title}/search")
async def search_book(title: str):
    return library.search_book(title)


@app.post("/books/{title}/add")
async def add_book(book: Book):
    return library.add_book(book)


@app.delete("/books/{title}/delete")
async def delete_book(title: str):
    return library.delete_book(title)


@app.patch("/books/{title}/status")
async def update_book_status(title: str, status: str):
    return library.update_book_status(title, status)


@app.get("/books/lib")
async def view_library():
    return library.view_library()


@app.get("/books/{title}/details")
async def view_book_details(title: str):
    return library.view_book_details(title)