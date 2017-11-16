from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    word = Column(String(100), unique=True)

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/translator'.format(os.environ["_MYSQL_USER"], os.environ["_MYSQL_PASSWORD"], os.environ["_MYSQL_HOST"], os.environ["_MYSQL_PORT"], os.environ["_APP_NAME"]), echo=int(os.environ["FLASK_DEBUG"]))
Base.metadata.create_all(engine)
