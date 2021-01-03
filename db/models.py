from sqlalchemy import Column, Integer, String

from db.engine import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, index=True)
