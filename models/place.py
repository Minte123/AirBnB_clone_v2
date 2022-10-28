#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from sqlalchemy import (
    Column, String, Integer, ForeignKey, Float, Table)
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review


if getenv("HBNB_TYPE_STORAGE", None) == "db":
    association_table = Table("place_amenity", Base.metadata,
                              Column("place_id", String(60),
                                     ForeignKey("places.id"),
                                     primary_key=True, nullable=False),
                              Column("amenity_id", String(60),
                                     ForeignKey("amenities.id"),
                                     primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    if getenv("HBNB_TYPE_STORAGE", None) == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenities = relationship(
            "Amenity", secondary=association_table, viewonly=False)
        reviews = relationship(
            "Review", backref="place", cascade="all,delete, delete-orphan")
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """ Return reviews in file storage system"""
            res = []
            rev = models.storage.all(Review)
            for value in rev.values():
                if value.place_id == self.id:
                    res.append(value)
            return res

        @property
        def amenities(self):
            """ get amenities from file storage"""
            return []

        @amenities.setter
        def amenities(self, value):
            """ set / append amenities """
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
