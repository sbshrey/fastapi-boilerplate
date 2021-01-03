from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError
from starlette.responses import JSONResponse, Response

from db.engine import db
from db.models import User
from schemas.users import UserBase, UserCreate

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('', response_model=List[UserBase], description='get all users')
def read_users():
    users = db.query(User).all()
    return users


@router.post('', description='create user', status_code=201)
def create_user(user: UserCreate):
    try:
        obj = User(**user.dict())
        db.add(obj)
        db.commit()
        return JSONResponse(status_code=HTTPStatus.CREATED)

    except IntegrityError:
        return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content={'error': 'user already exist'})


@router.patch('/{user_id}', description='update user', status_code=204, responses={204: {"data": None}},)
def update_user(user_id: int, user: UserCreate):
    try:
        db.query(User).filter(User.id == user_id).update({'name': user.name})
        db.commit()
        return Response(status_code=HTTPStatus.NO_CONTENT)
    except IntegrityError:
        return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content={'error': 'user does not exist'})


@router.get('/{name}', response_model=UserBase, description='get one user by name')
async def read_user(name: str):
    user = db.query(User).filter_by(name=name).one()
    return user


@router.delete('/{user_id}', description='delete one user by id', status_code=204)
def delete_user(user_id: int):
    try:
        db.query(User).filter_by(id=user_id).delete()
        return Response(status_code=HTTPStatus.NO_CONTENT)
    except IntegrityError:
        return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content={'error': 'user does not exist'})
