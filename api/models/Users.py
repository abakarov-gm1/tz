from databaseConf import Base
from sqlalchemy import Column, Integer, String


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # покупатель(buyer) / монтажник(installer)


