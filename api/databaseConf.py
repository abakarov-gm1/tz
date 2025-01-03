from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://tzApp:secret@db-postgres/tzApp", echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)


def get_session():
    return Session()

