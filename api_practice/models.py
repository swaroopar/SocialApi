from sqlalchemy import Column, String, Integer
from api_practice.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email_id = Column(String, unique=True)
    password = Column(String)
