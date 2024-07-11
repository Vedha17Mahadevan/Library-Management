Library Management System

This is a straightforward Library Management System designed for Admins/Librarians. It provides essential functionalities such as issuing books, searching for books using various parameters, updating book statuses, adding or deleting books, and viewing detailed information about books or the entire library.

Features:
Book Issuance: Allows users to issue books to patrons.
Advanced Search: Enables searching for books based on different parameters(e.g., name, genre , language).
Status Updates: Provides functionality to update the status of books (e.g., available, unavailable, borrowed).
Book Management: Includes features to add new books to the system or remove existing ones.
Comprehensive Views: Allows viewing detailed information about books individually or the entire library.

Technologies and Concepts:
Database: Utilizes a nested dictionary structure as the database.
Object-Oriented Programming (OOP): Implements OOP concepts for code organization and scalability
Functions: Incorporates functions to modularize operations within the system.

Implementation Details:
Framework: Developed using fastAPI.
IDE: Implemented in PyCharm for ease of development and debugging.

Usage:
Install Dependencies:
  pip install -r requirements.txt
Run the Application: 
  uvicorn main:app --reload
Access the API:
  Open your browser and go to http://localhost:8000/docs to view and interact with the API using Swagger UI.

Contributing:


License:
