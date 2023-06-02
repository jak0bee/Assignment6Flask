# Book Management System

by Jakub Suszwedyk (i6310933) and Marcell Dorko (i6326607)

## Introduction

The Book Management System is a microservices-based application designed to perform basic operations on a catalog of
books, manage the inventory of these books, and handle book orders. The system is implemented using Flask, a lightweight
web framework for Python.

The system consists of the following microservices:

1. [Book Catalog Service](book_management_system/catalog_service/catalog_specification.md): This service is responsible
   for performing CRUD operations on books. Each book has a unique identifier, title, author, and publication year.

2. [Book Inventory Service](book_management_system/inventory_service/inventory_specification.md): This service manages
   the inventory of books, tracking the available quantity of each book.

3. [Book Order Service](book_management_system/order_service/order_specification.md): This service handles book orders,
   each of which includes the book's unique identifier, the quantity ordered, and the date of the order.

## Starting the Services

To start all services, execute the `run_services.py` Python script. This script starts all the microservices and the api gateway.

## Unit Testing

The system comes with a set of unit tests for ensuring the functionality and reliability of the individual components.
Before executing the unit tests, ensure that all services are running as they are necessary for the correct operation of
the tests.

Please remember that all services must be running before executing the unit tests.
