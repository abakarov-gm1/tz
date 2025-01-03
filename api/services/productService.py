from models.products import Product

from databaseConf import get_session


def create_product(name, description, price=0, quantity=0):
    session = get_session()
    product = Product(name=name, description=description, price=price, quantity=quantity)
    session.add(product)
    session.commit()
    session.close()


def get_all_products():
    session = get_session()
    products = session.query(Product).all()
    return products
