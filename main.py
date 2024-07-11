from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date, timedelta

app = FastAPI()
def read_root():
    return {"message": "Welcome to Library Management System!"}


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
                                                          status='Available'),
            'Percy Jackson and the Titans Curse': Book(isbn='0-8086-5007-6', title='Percy Jackson and the Titans Curse',
                                                       author='Rick Riordan', genre='Fantasy', language='English',
                                                       status='Available'),
            'Percy Jackson and the Battle of Labyrinth': Book(isbn='0-4362-4883-2',
                                                              title='Percy Jackson and the Battle of Labyrinth',
                                                              author='Rick Riordan', genre='Fantasy',
                                                              language='English', status='Available'),
            'Percy Jackson and the Last Olympian': Book(isbn='0-4972-5506-5',
                                                        title='Percy Jackson and the Last Olympian',
                                                        author='Rick Riordan', genre='Fantasy', language='English',
                                                        status='Available'),
            "Harry Potter and the Sorcerer's Stone": Book(isbn='0-2878-1755-5',
                                                          title="Harry Potter and the Sorcerer's Stone",
                                                          author='J.K.Rowling', genre='Fantasy', language='English',
                                                          status='Available'),
            'Harry Potter and the Chamber of Secrets': Book(isbn='0-5555-6471-1',
                                                            title='Harry Potter and the Chamber of Secrets',
                                                            author='J.K.Rowling', genre='Fantasy', language='English',
                                                            status='Available'),
            'Harry Potter and the Prisoner of Azkaban': Book(isbn='0-1008-8983-2',
                                                             title='Harry Potter and the Prisoner of Azkaban',
                                                             author='J.K.Rowling', genre='Fantasy', language='English',
                                                             status='Available'),
            'Harry Potter and the Goblet of Fire': Book(isbn='0-8849-3881-6',
                                                        title='Harry Potter and the Goblet of Fire',
                                                        author='J.K.Rowling', genre='Fantasy', language='English',
                                                        status='Available'),
            'Harry Potter and the Goblet of Phoenix': Book(isbn='0-5701-7662-X',
                                                           title='Harry Potter and the Goblet of Phoenix',
                                                           author='J.K.Rowling', genre='Fantasy', language='English',
                                                           status='Available'),
            'Harry Potter and the Half-Blood Prince': Book(isbn='0-9734-1463-4',
                                                           title='Harry Potter and the Half-Blood Prince',
                                                           author='J.K.Rowling', genre='Fantasy', language='English',
                                                           status='Available'),
            'Harry Potter and the Deathly Hallow': Book(isbn='0-4419-2550-2',
                                                        title='Harry Potter and the Deathly Hallow',
                                                        author='J.K.Rowling', genre='Fantasy', language='English',
                                                        status='Available'),
            'Harry Potter and the Cursed Child': Book(isbn='0-9347-7389-0', title='Harry Potter and the Cursed Child',
                                                      author='J.K.Rowling', genre='Fantasy', language='English',
                                                      status='Available'),
            'To Kill A Mockingbird': Book(isbn='0-5168-1982-8', title='To Kill a Mockingbird', author='Harper Lee',
                                          genre='Southern Gothic', language='English', status='Available'),
            'The Diary of a Young Girl': Book(isbn='0-7086-8829-2', title='The Diary of a Young Girl',
                                              author='Anne Frank', genre='Autobiography', language='English',
                                              status='Available'),
            'Verity': Book(isbn='0-3829-2058-9', title='Verity', author='Colleen Hoover', genre='Thriller',
                           language='English', status='Available'),
            '1984': Book(isbn='0-3242-9694-0', title='1984', author='George Orwell', genre='Fiction',
                         language='English', status='Available'),
            'The Lord of Rings': Book(isbn='0-6459-7246-0', title='The Lord of Rings', author='J.R.R. Tolkein',
                                      genre='Fantasy', language='English', status='Available'),
            'The Book Thief': Book(isbn='0-4785-2218-5', title='The Book Thief', author='Markus Zusak', genre='Fiction',
                                   language='English', status='Available'),
            'Romeo and Juliet': Book(isbn='0-3872-0286-2', title='Romeo and Juliet', author='William Shakespeare',
                                     genre='Tragedy', language='English', status='Unavailable'),
            'Hamlet': Book(isbn='0-3995-9732-8', title='Hamlet', author='William Shakespeare', genre='Tragedy',
                           language='English', status='Unavailable'),
            'The Kite Runner': Book(isbn='0-6248-8208-X', title='The Kite Runner', author='Khaled Hosseini',
                                    genre='Fiction', language='English', status='Available'),
            'A Thousand Splendid Suns': Book(isbn='0-1349-6949-9', title='A Thousand Splendid Suns',
                                             author='Khaled Hosseini', genre='Fiction', language='English',
                                             status='Available'),
            'And the Mountains Echoed': Book(isbn='0-1027-8027-7', title='And the Mountains Echoed',
                                             author='Khaled Hosseini', genre='Fiction', language='English',
                                             status='Unavailable'),
            'The Hunger Games': Book(isbn='0-9244-8543-4', title='The Hunger Games', author='Suzanne Collins',
                                     genre='Fiction', language='English', status='Available'),
            'The Alchemist': Book(isbn='0-3185-7904-9', title='The Alchemist', author='Paulo Coelho', genre='Classics',
                                  language='English', status='Available'),
            'The Odyssey': Book(isbn='0-4829-1214-6', title='The Odyssey', author='Homer', genre='Poetry',
                                language='English', status='Unavailable'),
            'Adventures of Tom Sawyer': Book(isbn='0-7065-1251-0', title='Adventures of Tom Sawyer',
                                             author='Mark Twain', genre='Fantasy', language='English',
                                             status='Available'),
            'The Tale of Two Cities': Book(isbn='0-7374-2013-8', title='The Tale of Two Cities',
                                           author='Charles Dickens', genre='Historical Novel', language='English',
                                           status='Available'),
            'Life of Pi': Book(isbn='0-5144-2272-6', title='Life of Pi', author='Yann Martel', genre='Fiction',
                               language='English', status='Available'),
            'The Da Vinci Code': Book(isbn='0-3939-6778-6', title='The Da Vinci Code', author='Dan Brown',
                                      genre='Thriller', language='English', status='Available'),
            "Alice's Adventures in Wonderland": Book(isbn='0-8676-7658-2', title="Alice's Adventures in Wonderland",
                                                     author='Lewis Carroll', genre='Fantasy', language='English',
                                                     status='Available'),
            'The Lion, the Witch and the Wardrobe': Book(isbn='0-6397-5281-0',
                                                         title='The Lion, the Witch and the Wardrobe',
                                                         author='CS Lewis', genre='Fantasy', language='English',
                                                         status='Available'),
            'The Northern Lights': Book(isbn='0-5067-4655-0', title='The Northern Lights', author='Philip Pullman',
                                        genre='Fantasy', language='English', status='Available'),
            'Matilda': Book(isbn='0-8359-4549-9', title='Matilda', author='Roald Dahl and Quentin Blake',
                            genre='Fantasy', language='English', status='Available'),
            'Little Women': Book(isbn='0-3226-3006-1', title='Little Women', author='Louisa May Alcott',
                                 genre='Fiction', language='English', status='Available'),
            'Charlie and the Chocolate Factory': Book(isbn='0-7604-4527-3', title='Charlie and the Chocolate Factory',
                                                      author='Roald Dahl', genre='Fantasy', language='English',
                                                      status='Unavailable'),
            'I Want My Hat Back': Book(isbn='0-3948-2983-2', title='I Want My Hat Back', author='Jon Klassen',
                                       genre='Fantasy', language='English', status='Unavailable'),
            'The Three Robbers': Book(isbn='0-1824-9425-X', title='The Three Robbers', author='Tom Ungerer',
                                      genre='Fantasy', language='English', status='Unavailable'),
            'The Snowy Day': Book(isbn='0-3323-6560-3', title='The Snowy Day', author='Ezra Jack Keats',
                                  genre='Fantasy', language='English', status='Unavailable'),
            'Momo': Book(isbn='0-1158-1872-3', title='Momo', author='Michael Ende', genre='Fantasy', language='English',
                         status='Unavailable'),
            'The Tale of Peter Rabbit': Book(isbn='0-4066-0025-2', title='The Tale of Peter Rabbit',
                                             author='Beatrix Potter', genre='Fantasy', language='English',
                                             status='Available'),
            'The Jungle Book': Book(isbn='0-7125-1500-3', title='The Jungle Book', author='Rudyard Kipling',
                                    genre='Fantasy', language='English', status='Available'),
            'The Cat in the Hat': Book(isbn='0-7125-1500-3', title='The Cat in the Hat', author='Dr Seuss',
                                       genre='Fantasy', language='English', status='Available'),
            'The Immortals of Meluha': Book(isbn='0-8016-6201-X', title='The Immortals of Meluha',
                                            author='Amish Tripathi', genre='Fantasy', language='English',
                                            status='Available'),
            'The Secret of Nagas': Book(isbn='0-2086-2879-7', title='The Secret of Nagas', author='Amish Tripathi',
                                        genre='Fantasy', language='English', status='Available'),
            'The Oath of Vayuputras': Book(isbn='0-4493-9461-1', title='The Oath of Vayuputras',
                                           author='Amish Tripathi', genre='Fantasy', language='English',
                                           status='Available'),
            'Ram:Scion of Ikshvaku': Book(isbn='0-9214-8749-5', title='Ram:Scion of Ikshvaku', author='Amish Tripathi',
                                          genre='Fantasy', language='English', status='Available'),
            'Sita: Warrior of Mithila': Book(isbn='0-3835-9320-4', title='Sita: Warrior of Mithila',
                                             author='Amish Tripathi', genre='Fantasy', language='English',
                                             status='Available'),
            'Raavan: Enemy of Aryavarta': Book(isbn='0-6008-4326-2', title='Raavan: Enemy of Aryavarta',
                                               author='Amish Tripathi', genre='Fantasy', language='English',
                                               status='Available'),
            'War of Lanka': Book(isbn='0-1127-6854-7', title='War of Lanka', author='Amish Tripathi', genre='Fantasy',
                                 language='English', status='Available'),
            'Legend of Suheldev: The King Who Saved India': Book(isbn='0-3733-7460-7',
                                                                 title='Legend of Suheldev: The King Who Saved India',
                                                                 author='Amish Tripathi', genre='Fantasy',
                                                                 language='English', status='Available'),
            'Malgudi Days': Book(isbn='0-5338-4200-X', title='Malgudi Days', author='R.K. Narayan', genre='Fiction',
                                 language='English', status='Available'),
            'The Room on the Roof': Book(isbn='0-7959-2917-X', title='The Room on the Roof', author='Ruskin Bond',
                                         genre='Fiction', language='English', status='Available'),
            'The God of Small Things': Book(isbn='0-5714-6376-2', title='The God of Small Things',
                                            author='Arundathi Roy', genre='Drama', language='English',
                                            status='Unavailable'),
            'The 3 Mistakes of My Life': Book(isbn='0-8404-0073-X', title='The 3 Mistakes of My Life',
                                              author='Chetan Bhagat', genre='Fiction', language='English',
                                              status='Unavailable'),
            'One Night @ the Call Centre': Book(isbn='0-1189-6303-1', title='One Night @ the Call Centre',
                                                author='Chetan Bhagat', genre='Fiction', language='English',
                                                status='Unavailable'),
            'The Girl in Room 105': Book(isbn='0-7097-6787-0', title='The Girl in Room 105', author='Chetan Bhagat',
                                         genre='Thriller', language='English', status='Available'),
            'One Arranged Murder': Book(isbn='0-9235-3038-X', title='One Arranged Murder', author='Chetan Bhagat',
                                        genre='Thriller', language='English', status='Available'),
            '400 Days': Book(isbn='0-5466-1351-9', title='400 Days', author='Chetan Bhagat', genre='Thriller',
                             language='English', status='Available'),
            'I Too Had A Love Story': Book(isbn='0-8132-8409-0', title='I Too Had A Love Story',
                                           author='Ravinder Singh', genre='Romance', language='English',
                                           status='Available'),
            'Like It Happened Yesterday': Book(isbn='0-5520-2359-0', title='Like It Happened Yesterday',
                                               author='Ravinder Singh', genre='Romance', language='English',
                                               status='Available'),
            'Your Dreams Are Mine Now': Book(isbn='0-7353-7106-7', title='Your Dreams Are Mine Now',
                                             author='Ravinder Singh', genre='Romance', language='English',
                                             status='Available'),
            'Tell Me A Story': Book(isbn='0-2080-0055-0', title='Tell Me A Story', author='Ravinder Singh',
                                    genre='Romance', language='English', status='Available'),
            'Will You Still Love Me?': Book(isbn='0-1123-3373-7', title='Will You Still Love Me?',
                                            author='Ravinder Singh', genre='Romance', language='English',
                                            status='Available'),
            'Wake Up, Life is Calling': Book(isbn='0-1726-3573-0', title='Wake Up, Life is Calling',
                                             author='Preethi Shenoy', genre='Fiction', language='English',
                                             status='Available'),
            'Wings of Fire': Book(isbn='0-4001-8693-4', title='Wings of Fire', author='A.P.J. Abdul Kalam',
                                  genre='Autobiography', language='English', status='Available'),
            'A Study in Scarlet': Book(isbn='0-1581-8577-3', title='A Study in Scarlet',
                                       author='Sir Arthur Conan Doyle', genre='Thriller', language='English',
                                       status='Available'),
            'The Hound of Baskervilles': Book(isbn='0-4722-3104-9', title='The Hound of Baskervilles',
                                              author='Sir Arthur Conan Doyle', genre='Thriller', language='English',
                                              status='Available'),
            'War and Peace': Book(isbn='0-4722-3104-9', title='War and Peace', author='Leo Tolstoy', genre='Fiction',
                                  language='English', status='Available'),
            'Gaban': Book(isbn='0-5823-5880-9', title='Gaban', author='Munshi Premchand', genre='Fiction',
                          language='Hindi', status='Available'),
            'Chandrakanta': Book(isbn='0-4655-1545-2', title='Chandrakanta', author='Devaki Nadan Khatri',
                                 genre='Historical Novel', language='Hindi', status='Available'),
            'Godan': Book(isbn='0-6121-0344-7', title='Godan', author='Munshi Premchand', genre='Fiction',
                          language='Hindi', status='Available'),
            'Raag Darbari': Book(isbn='0-7428-3184-1', title='Raag Darbari', author='Shreelaal Shukla',
                                 genre='Satirical Novel', language='Hindi', status='Available'),
            'Karmabhoomi': Book(isbn='0-3131-9972-8', title='Karmabhoomi', author='Munshi Premchand', genre='Classics',
                                language='Hindi', status='Available'),
            'Gora': Book(isbn='0-2594-3474-4', title='Gora', author='Ravindranath Tagore', genre='Fiction',
                         language='Hindi', status='Available'),
            'Joothan': Book(isbn='0-2265-1246-0', title='Joothan', author='Om Prakash Valmiki', genre='Autobiography',
                            language='Hindi', status='Available'),
            'Madhushala': Book(isbn='0-6363-8786-0', title='Madhushala', author='Harivansh Rai Bachchan',
                               genre='Poetry', language='Hindi', status='Available'),
            'Tamas': Book(isbn='0-3119-8859-8', title='Tamas', author='Bhisham Sahni', genre='Fiction',
                          language='Hindi', status='Available'),
            'Randamoozham': Book(isbn='0-2492-9072-3', title='Randamoozham', author='M.T Vasudevan Nair',
                                 genre='Mythology', language='Malayalam', status='Unavailable'),
            'Pathummayude Aadu': Book(isbn='0-3363-9327-X', title='Pathummayude Aadu',
                                      author='Vaikom Muhhammad Basheer', genre='Fiction', language='Fiction',
                                      status='Available'),
            'Aadujeevitham': Book(isbn='0-7273-0884-X', title='Aadujeevitham', author='Benyamin', genre='Ficiton',
                                  language='Malayalam', status='Available'),
            'Ente Katha': Book(isbn='0-2442-0191-9', title='Ente Katha', author='Kamala Suraiyya Das',
                               genre='AutoBiography', language='Malayalam', status='Available'),
            'Oru Desathinde Katha': Book(isbn='0-3654-1258-9', title='Oru Desathinde Katha', author='S.K. Pottekkat',
                                         genre='Fiction', language='Malayalam', status='Available'),
            'Nashtapetta Neelambari': Book(isbn='0-4052-9964-8', title='Nashtapetta Neelambari',
                                           author='Kamala Suraiyya Das', genre='Short Story', language='Malayalam',
                                           status='Available'),
            'Ini Njan Urangatte': Book(isbn='0-9967-0667-4', title='Ini Njan Urangatte', author='P.K Balakrishnan',
                                       genre='Mythology', language='Malayalam', status='Available'),
            'Indulekha': Book(isbn='0-7679-4893-9', title='Indulekha', author='O. Chandu Menon', genre='Classics',
                              language='Malayalam', status='Available'),
            'Ponniyin Selvan': Book(isbn='0-8043-0976-0', title='Ponniyin Selvan', author='Kalki', genre='Drama',
                                    language='Tamil', status='Available'),
            'Oru Puliyamarathin Kathai': Book(isbn='0-9119-8268-X', title='Oru Puliyamarathin Kathai',
                                              author='Sundara Ramaswamy', genre='Novel', language='Tamil',
                                              status='Unavailable'),
            'Sila Nerangalil Sila Manithargal': Book(isbn='0-8737-0120-8', title='Sila Nerangalil Sila Manithargal',
                                                     author='Jayakanthan', genre='Fiction', language='Tamil',
                                                     status='Available'),
            'Kallikaattu Ithigaasam': Book(isbn='0-6856-4710-2', title='Kallikaattu Ithigaasam', author='Vairamuthu',
                                           genre='Fiction', language='Tamil', status='Available'),
            'Oswal Question Bank Hindi Class 10': Book(isbn='0-3847-4992-5', title='Oswal Question Bank Hindi Class 10',
                                                       author='Oswal Publishers', genre='Study Material',
                                                       language='Hindi', status='Available'),
            'R.D. Sharma Mathematics Class 10': Book(isbn='0-1563-3909-9', title='R.D. Sharma Mathematics Class 10',
                                                     author='R.D. Sharma', genre='Study Material', language='English',
                                                     status='Available'),
            'Xam Idea Science Class 10': Book(isbn='0-2268-7239-4', title='Xam Idea Science Class 10',
                                              author='Xam Idea', genre='Study Material', language='English',
                                              status='Available'),
            'Togetherwith Social Science Class 10': Book(isbn='0-7207-1416-8',
                                                         title='Togetherwith Social Science Class 10',
                                                         author='Togetherwith', genre='Study Material',
                                                         language='English', status='Available'),
            'Golden English Class 10': Book(isbn='0-5675-5864-9', title='Golden English Class 10', author='Golden',
                                            genre='Study Material', language='English', status='Available'),
            'NCERT Biology Class 12': Book(isbn='0-6135-4977-5', title='NCERT Biology Class 12', author='NCERT',
                                           genre='Study Material', language='English', status='Available'),
            'All in One Physics Class 12': Book(isbn='0-3892-3059-6', title='All in One Physics Class 12',
                                                author='All in One', genre='Study Material', language='English',
                                                status='Available'),
            'Oswal Question Bank Mathematics Class 12': Book(isbn='0-7367-1616-5',
                                                             title='Oswal Question Bank Mathematics Class 12',
                                                             author='Oswal Publishers', genre='Study Material',
                                                             language='English', status='Available'),
            'All in One Chemistry Class 12': Book(isbn='0-1564-2938-1', title='All in One Chemistry Class 12',
                                                  author='All in One', genre='Study Material', language='English',
                                                  status='Available'),
            'NCERT Macro-Economics Class 12': Book(isbn='0-9359-1433-1', title='NCERT Macro-Economics Class 12',
                                                   author='NCERT', genre='Study Material', language='English',
                                                   status='Available'),
            'Advanced Engineering Mathematics Edition 2012': Book(isbn='0-1163-4321-4',
                                                                  title='Advanced Engineering Mathematics Edition 2012',
                                                                  author='Peter V. O\'Neil', genre='Study Material',
                                                                  language='English', status='Unavailable'),
            'Concepts of Modern Physics, 6th Edition': Book(isbn='0-9568-2040-9',
                                                            title='Concepts of Modern Physics, 6th Edition',
                                                            author='Aurthur Beiser', genre='Study Material',
                                                            language='English', status='Available'),
            'Programming With C': Book(isbn='0-3428-7836-0', title='Programming With C', author='Bryon Gottfried',
                                       genre='Study Material', language='English', status='Available'),
            'Environmental Engineering and Management': Book(isbn='0-1016-2180-9',
                                                             title='Environmental Engineering and Management',
                                                             author='Suresh K. Dhameja', genre='Study Material',
                                                             language='English', status='Available'),
            'Engineering Chemistry, Second Edition': Book(isbn='0-7778-6644-7',
                                                          title='Engineering Chemistry, Second Edition',
                                                          author='Roy Varghese', genre='Study Material',
                                                          language='English', status='Available'),
            'Digital Logic and Computer Design': Book(isbn='0-1512-0972-3', title='Digital Logic and Computer Design',
                                                      author='M. Morris Mano', genre='Study Material',
                                                      language='English', status='Available'),
            'Professional Communication': Book(isbn='0-1052-6293-5', title='Professional Communication',
                                               author='Meenakshi Raman and Sangeetha Sharma', genre='Study Material',
                                               language='English', status='Available'),
            'Manufacturing Technology - I': Book(isbn='0-6122-6171-9', title='Manufacturing Technology - I',
                                                 author='Gowri P. Hariharan', genre='Study Material',
                                                 language='English', status='Available')
        }

    def add_book(self, book: Book):
        if book.title in self.books:
            raise HTTPException(status_code=400, detail="Book already exists in the library")
        self.books[book.title] = book
        return book.title + " has been added to the library"

    def delete_book(self, title: str):
        if title not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        del self.books[title]
        return title + " has been deleted from the library"

    def search_book_name(self, title: str):
        if title not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        return self.books[title].status

    def search_book_genre(self, genre: str):
        book_genre=[]
        for books in self.books.values():
            if books.genre == genre:
                book_genre.append(books.title)
        if not book_genre:
            raise HTTPException(status_code=404, detail="Genre not found")
        return book_genre

    def search_book_language(self, language: str):
        book_lang=[]
        for books in self.books.values():
            if books.language == language:
                book_lang.append(books.title)
        if not book_lang:
            raise HTTPException(status_code=404, detail="Language not found")
        return book_lang


    def update_book_status(self, title: str, status: str):
        if title not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        self.books[title].status = status
        return "The status of "+title+" has been updated"

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
        self.books[title].status = "Issued to",student_id
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


@app.get("/books/{title}/searchname")
async def search_book_name(title: str):
    return library.search_book_name(title)

@app.get("/books/{title}/searchgenre")
async def search_book_genre(genre: str):
    return library.search_book_genre(genre)

@app.get("/books/{title}/searchlanguage")
async def search_book_language(language: str):
    return library.search_book_language(language)

@app.post("/books/{title}/add")
async def add_book(book: Book):
    return library.add_book(book)


@app.delete("/books/{title}/delete")
async def delete_book(title: str):
    return library.delete_book(title)


@app.patch("/books/{title}/status")
async def update_book_status(title: str, status: str):
    return library.update_book_status(title, status)


@app.get("/books/{title}/details")
async def view_book_details(title: str):
    return library.view_book_details(title)

@app.get("/books/lib")
async def view_library():
    return library.view_library()
