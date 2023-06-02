# Book Catalog Service API

The book catalog service provides endpoints for managing the books in the catalog. The server runs on port 3001.

## Endpoints

### GET /catalog/{book_id}

Retrieves a book from the catalog.

**Parameters**

- `book_id`: ID of the book (integer)

**Responses**

- `200`: Successful operation. Returns the requested book.
- `404`: Book not found.

---

### POST /catalog/create

Creates a new book in the catalog.

**Parameters**

- `title`: Title of the book (string, required)
- `author`: Author of the book (string, required)
- `publication_year`: Year of book publication (integer, required)

**Responses**

- `201`: Successful operation. Returns the created book.
- `400`: Invalid input. Missing required parameters or invalid data type.
- `500`: Internal server error. Unable to create book.

---

### DELETE /catalog/delete

Deletes a book from the catalog.

**Parameters**

- `book_id`: ID of the book to delete (integer, required)

**Responses**

- `204`: Successful operation. Book was successfully deleted.
- `404`: Invalid input. Book not found.

---

### PUT /catalog/update

Updates an existing book in the catalog.

**Parameters**

- `book_id`: ID of the book to update (integer, required)
- `title` (optional): New title of the book (string)
- `author` (optional): New author of the book (string)
- `publication_year` (optional): New year of publication (integer)

**Responses**

- `200`: Successful operation. Returns the updated book.
- `400`: Invalid input. Missing required parameters or invalid data type.
- `404`: Invalid input. Book not found.
