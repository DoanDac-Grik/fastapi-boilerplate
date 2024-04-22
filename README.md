# Boilerplate for MVC with FastAPI + SQLModel

## Tech

- FastAPI: Python
- Database: MySQL
- ORM: SQLModel

## Project structure

```bash
└───src
│    ├───apis
│    │   ├───ping                   # 3 layers, almost similar MVC model
│    │   │   └───routers.py
│    │   │   └───models.py
│    │   │   └───controllers.py
│    |   └───__init__.py            # Wrap all routers
│    ├───common                     # Include shared uses
│    │   └───constants.py
│    │   └───response.py
│    ├───configs                    # For configurations
│    │   └───database.py
│    │   └───env.py
│    ├───utils                      # Support functions
│    │   └───logger.py
│    │   └───seed_data.py
│    └───app.py
├────asgi.py
└────requirement.txt
```

## Basic instructions/explainations

### With being almost similar to MVC - 3 layers, is there any problems?

3 layers help to simple implementation. No need to separate to complex layers, focus on the requirement with rapid development.

Of course, to increase the effectiveness of the model, we need some additional folders, it's outside `/apis` folder. For example, with complex logical handlings in a library, we will separate them to `/libs` to handle, then call them in controller, or some useful functions are often resued, we will move them to `/utils`

### How to validate?

- Validate `Param`: FastAPI supports validate directly in argument of function bellow `@router`

```python
# URI: localhost:8000/ping/5

@router.get(
    "/ping/{test}",
    status_code=status.HTTP_200_OK,
)
def check_health(test: Annotated[int, Path(title="User ID")]):
    return "pong"

```

- Validate `Query`: FastAPI supports validate directly in argument of function bellow `@router`

```python
# URI: localhost:8000/ping?test=5

@router.get(
    "/ping",
    status_code=status.HTTP_200_OK,
)
def check_health(test: Annotated[int | None, Query(gt=0)] = 1):
    return "pong"

```

- Validate `Body`: we use SQLModel to create model likes "DTO" to validate

```python
# URI: localhost:8000/ping

class Body(SQLModel):
    name: str = Field(max_length=50)
    gender: Gender

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Join",
                "gender": "male"
            }
        }

@router.post(
    "/ping",
    status_code=status.HTTP_200_OK,
)
def check_health(payload: Body):
    return "pong"
```

### Response format

- Successful response format:

```json
{
  "data": {
    "id": 1,
    "name": "John Smith"
  }
}
```

- Successful response format with pagination:

```json
{
  "data": [
    {
      "id": 1,
      "name": "John Smith"
    },
    {
      "id": 1,
      "name": "John Smith"
    }
  ],
  "limit": 1,
  "page": 1,
  "total_pages": 1
}
```

- Error response format:

```json
{
  "detail": "User not found"
}
```

For validtion errors, they will be more details because of Pydantic:

```json
{
  "detail": [
    {
      "loc": ["string", 0],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

## Installation & Running

To init virtual environment

```sh
python -m venv env
```

Access to the virtual environment

```sh
env\Scripts\activate # for windows
source env/bin/activate # for linux and mac
```

Install dependencies

```sh
pip install -r requirement.txt
```

Run server

```sh
py asgi.py
```

## TODO:

- Dockernize application
