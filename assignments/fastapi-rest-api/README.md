# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI, using HTTP methods, Pydantic models, status codes, and automatic API documentation. The API will manage a small in-memory catalog of books.

## 📝 Tasks

### 🛠️ Create the API and list books

#### Description
Install FastAPI and Uvicorn, run the provided starter code, and create the first endpoint for the book catalog. Use the interactive documentation at `/docs` to explore and test the API.

Start the server with:

```bash
python -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

#### Requirements
The completed program must:

- Keep the existing `GET /health` endpoint and return a successful response from it
- Implement `GET /books` to return all books as a JSON list
- Return an empty list when the catalog has no books
- Verify both endpoints using `/docs`

### 🛠️ Add and retrieve books

#### Description
Define Pydantic models for creating and returning books. Add endpoints to create a book and retrieve one book by its ID.

#### Requirements
The completed program must:

- Represent each book with an integer `id`, a non-empty `title`, and a non-empty `author`
- Implement `POST /books` and assign a unique ID to each new book
- Return the created book and use HTTP status `201 Created`
- Implement `GET /books/{book_id}` and return HTTP `404 Not Found` when the ID does not exist
- Let FastAPI reject invalid request data with a clear validation response

### 🛠️ Complete the book CRUD API

#### Description
Add the remaining update and delete operations, then test the full lifecycle of a book through the API. The catalog may be stored in memory, so its contents do not need to persist after the server stops.

#### Requirements
The completed program must:

- Implement `PUT /books/{book_id}` to update a book's title and author
- Implement `DELETE /books/{book_id}` to remove a book and return an appropriate success status
- Return HTTP `404 Not Found` when an update or delete targets a missing book
- Use the appropriate HTTP methods and status codes for each operation
- Demonstrate creating, listing, retrieving, updating, and deleting a book in `/docs`
