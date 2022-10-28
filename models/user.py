#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE", None) == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship("Review",
                               backref="user")
        places = relationship("Place",
                              backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """ initialize user"""
        super().__init__(*args, **kwargs)
