from databaseConf import get_session
from models.Users import User


def create_user(name, email, hashed_password, role):
    session = get_session()
    new_user = User(name=name, email=email, password=hashed_password, role=role)
    session.add(new_user)
    session.commit()
    session.close()


def get_user_by_name(user_name: str):
    session = get_session()
    return session.query(User).filter(User.name == user_name).first()