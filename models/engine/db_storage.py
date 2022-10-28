#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        if not(cls in classes or cls in classes.values()):
            res = list(self.__session().query(State).all())
            res.extend(self.__session().query(User).all())
            res.extend(self.__session().query(Place).all())
            res.extend(self.__session().query(City).all())
            res.extend(self.__session().query(Review).all())
            res.extend(self.__session().query(Amenity).all())
            for obj in res:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                new_dict[key] = obj
        else:
            try:
                if isinstance(cls, str):
                    cls = eval(cls)
                res = list(self.__session().query(cls))
                for obj in res:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    new_dict[key] = obj
            except Exception:
                new_dict = {}
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session().add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session().commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session().delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(sess_factory)
        self.__session = session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
