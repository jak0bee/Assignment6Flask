# Book Inventory Service API

The book inventory service provides endpoints for managing the inventory of the books. The server runs on port 3002.

## Endpoints

### GET /inventory

Retrieves all books in the inventory.

**Responses**

- `200`: Successful operation. Returns a list of all books in the inventory.

---

### POST /inventory/create

Adds a book to the inventory.

**Parameters**

- `book_id`: ID of the book (integer, required)

**Responses**

- `201`: Successful operation. Returns the created inventory item.
- `400`: Invalid input. Missing required parameter.

---

### PUT /inventory/update

Updates the quantity of a book in the inventory.

**Parameters**

- `book_id`: ID of the book to update (integer, required)
- `quantity`: New quantity of the book (integer, required)

**Responses**

- `200`: Successful operation. Returns the updated inventory item.
- `400`: Invalid input. Missing required parameters or invalid data type.
