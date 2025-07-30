# Employee Data Management API

This project is a simple Employee Data Management REST API built with **FastAPI**, **SQLAlchemy**, and **SQLite**. It allows you to create, read, update, and delete (CRUD) employee records.
## Features

- Add new employees
- View all employees
- View a specific employee by ID
- Update employee details
- Delete employees

## Tech Stack
- Python 3.7+
- FastAPI
- SQLAlchemy
- SQLite (local file database)
- Pydantic

## Getting Started
### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd employee-data
```
### 2. Create a Virtual Environment (Recommended)

```sh
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac
```
### 3. Install Dependencies

```sh
pip install fastapi uvicorn sqlalchemy pydantic
```
### 4. Run the API Server

```sh
uvicorn EmployeeData:app --reload
```
The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 5. API Documentation
FastAPI provides interactive API docs at:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints
### Create Employee

- **POST** `/employees/`
  - **Body:**
    ```json
    {
      "name": "John Doe",
      "age": 30,
      "department": "Engineering"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Employee created successfully",
      "employee": {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "department": "Engineering"
      }
    }
    ```

### Get All Employees

- **GET** `/employees/`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "department": "Engineering"
      },
      ...
    ]
    ```
### Get Employee by ID

- **GET** `/employees/{employee_id}`
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "age": 30,
      "department": "Engineering"
    }
    ```

### Update Employee

- **PUT** `/employees/{employee_id}`
  - **Body:**
    ```json
    {
      "name": "Jane Smith",
      "age": 28,
      "department": "HR"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Employee updated successfully",
      "employee": {
        "id": 1,
        "name": "Jane Smith",
        "age": 28,
        "department": "HR"
      }
    }
    ```

### Delete Employee

- **DELETE** `/employees/{employee_id}`
  - **Response:**
    ```json
    {
      "message": "Employee deleted successfully"
    }
    ```

## Database

The API uses a local SQLite database file named `employees.db`. The database and table are created automatically on first run.

## Notes

- For development/testing only. Not intended for production use.
- You can use tools like [Postman](https://www.postman.com/) or the built-in Swagger UI to test the API.

## License

MIT License
