# Book Management System

by Software Engineering Assignments 55: Jakub Suszwedyk (i6310933) and Marcell Dorko (i6326607)

## Introduction

The Book Management System is a microservices-based application designed to perform basic operations on a catalog of books, manage the inventory of these books, and handle book orders. The system is implemented using Flask.

The system consists of the following microservices:

1. [Book Catalog Service](book_management_system/catalog_service/catalog_specification.md): This service is responsible
   for performing CRUD operations on books.

2. [Book Inventory Service](book_management_system/inventory_service/inventory_specification.md): This service manages
   the inventory of books, tracking the  quantity of each book.

3. [Book Order Service](book_management_system/order_service/order_specification.md): This service handles book orders.

Each sevice has its own md file and a specification defined in a yaml file.

## Starting the Services

To start the services, execute the `run_services.py` Python script. This script starts all the microservices and the api gateway.

## Unit Testing

The system comes with a set of unit tests for ensuring the functionality and reliability of the individual components.

The files containing the unittests are in the `test` directory.

Please remember that all services must be running before executing the unit tests in order for the results to be meaningful.

The screenshots of the unittests being successful are in the `test_results` directory.
