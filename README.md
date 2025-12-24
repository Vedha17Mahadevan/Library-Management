# 📚 Library Management System

This is a straightforward **Library Management System** designed for **Admins / Librarians**.  
It provides essential functionalities such as issuing books, searching for books using various parameters, updating book statuses, managing the book collection, and viewing detailed information about books or the entire library.

---

## ✨ Features

- **Book Issuance**  
  Allows books to be issued to patrons.

- **Advanced Search**  
  Search for books using multiple parameters such as **name, genre, and language**.

- **Status Updates**  
  Update book availability status (available, unavailable, borrowed).

- **Book Management**  
  Add new books to the system or delete existing ones.

- **Comprehensive Views**  
  View detailed information for individual books or the entire library collection.

---

## 🛠️ Technologies & Concepts

- **Database**  
  Uses a **nested dictionary structure** as an in-memory database.

- **Object-Oriented Programming (OOP)**  
  Implements OOP principles for better organization and scalability.

- **Functions**  
  Modular functions are used to handle different system operations.

---

## ⚙️ Implementation Details

- **Framework:** FastAPI  
- **IDE:** PyCharm  

---

## 🚀 Usage

### Install Dependencies
```bash
pip install -r requirements.txt
```
### Run the Application
```bash
uvicorn main:app --reload
```
### Access the API
```bash
http://localhost:8000/docs
```
