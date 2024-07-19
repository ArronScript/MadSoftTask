
# Memes API

This is a simple API for managing a collection of memes. It consists of four services: a public API service with business logic, a media service for working with media files using S3-compatible storage (e.g. MinIO), a database service for working with a relational database (e.g. PostgreSQL) and a documentation service for API documentation using Swagger/OpenAPI.

---------------------------------------------------------------------------------

Это простой API для управления коллекцией мемов. Он состоит из четырех сервисов: общедоступного API-сервиса с бизнес-логикой, медиа-сервиса для работы с медиафайлами с использованием S3-совместимого хранилища (например, MinIO), сервиса базы данных для работы с реляционной базой данных (например, PostgreSQL) и сервиса документации для Документация API с использованием Swagger/OpenAPI.


## Functionality

- GET /memes: Get a list of all memes (with pagination).
- GET /memes/{id}: Get a specific mem by its ID.
- POST /memes: Add a new mem (with an image and text).
- PUT /memes/{id}: Update an existing mem.
- DELETE /memes/{id}: Delete a mem.

## Requirements

- Use a relational database for data storage.
- Handle errors and validate input data.
- Use Swagger/OpenAPI for API documentation.
- Write at least several unit tests for checking the main functionality.
- Write a Readme that explains the functionality of the project and instructions for local development.
- The project should consist of at least: 1 public API service, 1 private API service for images, 1 database service, 1 S3-storage service.
- Write a docker-compose.yml for running the project.

## Local development
1. docker-compose up
2. open http://127.0.0.1:8000/docs

