# fastapi-boilerplate
Boilerplate of REST API Server using FastAPI, Poetry, SQLAlchemy, Alembic, Docker


## Spec
```
Python==3.9.0
PyMySQL
Alembic
SQLAlchemy
FastAPI
```

## Installation

## Run
### Run server
```shell script
uvicorn main:app --reload
```

### Run test
```shell script
pytest
```

## Database
Use MySQL as database, using SQLAlchemy as ORM and using Alembic as migration tool.

### Migration
1. Create Migration file  
```shell script
alembic autogenerate
```

2. Run migration
```shell script
alembic 
```

## Structure
```shell script
main.py --runserver
```
