# Todo List API

This is a simple REST API built with FastAPI to manage a Todo list.

## Features

- List all todos
- Create a new todo
- Get a single todo by ID
- Update a todo by ID
- Delete a todo by ID

## Endpoints

| Method | Endpoint       | Description               |
|--------|----------------|---------------------------|
| GET    | /todos         | List all todos            |
| POST   | /todos         | Create a new todo         |
| GET    | /todos/{id}    | Get a todo by ID          |
| PUT    | /todos/{id}    | Update a todo by ID       |
| DELETE | /todos/{id}    | Delete a todo by ID       |

## Screenshots

### FastAPI Server Terminal Output  
![FastAPI Server Terminal Output](MAIN_TERMINAL_OUTPUT.png)

### Swagger UI Documentation  
![Swagger UI Documentation](Swagger_UI_screenshot.png)

### GET /todos Test  
![GET /todos Test](GET_TEST.png)

### POST /todos Test  
![POST /todos Test](POST_TEST.png)

### DELETE /todos Test  
![DELETE /todos Test](DELETE_TEST.png)




## How to Run

1. Install dependencies:

```bash
pip install fastapi uvicorn
uvicorn main:app --reload




