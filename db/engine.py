from sqlalchemy import create_engine, databases
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://dev:dev@localhost:3306/pilot'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Session_ = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = Session_()
# database = databases.Database(SQLALCHEMY_DATABASE_URL)
