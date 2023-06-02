# Book Order Service API

The book order service provides endpoints for managing the orders of the books. The server runs on port 3003.

## Endpoints

### GET /orders/get

Retrieves all orders.

**Responses**

- `200`: Successful operation. Returns a list of all orders.

---

### POST /orders/create

Creates a new book order.

**Parameters**

- `book_id`: ID of the book (integer, required)
- `quantity`: Quantity of the book to order (integer, required)
- `date`: Date of the order (string, required)

**Responses**

- `201`: Successful operation. Returns the created order.
- `400`: Invalid input. Missing required parameters or invalid data type.
- `500`: Server error. Unable to retrieve or update inventory.
