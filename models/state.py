#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE", None) == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            res = []
            all_cities = models.storage.all("City")
            for value in all_cities.values():
                if value.state_id == self.id:
                    res.append(value)
            return res
