from databaseConf import Base
from sqlalchemy import Column, Integer, String, Text


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=True)
    quantity = Column(Integer, nullable=True)


