#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

CLASSES = {
    "User": User,
    "Place": Place,
    "City": City,
    "Review": Review,
    "Amenity": Amenity,
    "State": State
}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls not in CLASSES or cls not in CLASSES.values():
            return FileStorage.__objects
        res = {}
        if isinstance(cls, str):
            cls = eval(cls)
        for key, obj in FileStorage.__objects.items():
            if cls == type(obj):
                res[key] = obj
        return res

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        value = obj
        FileStorage.__objects[key] = value

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            temp = {}
            if FileStorage.__objects:
                my_dict = FileStorage.__objects
                for key, val in my_dict.items():
                    val = val.to_dict()
                    for k, v in val.items():
                        if isinstance(v, datetime):
                            val[k] = datetime.isoformat(v)
                    temp[key] = val
            json.dump(temp, f)

    def delete(self, obj=None):
        """ Delete object """
        if obj:
            cls_name = obj.__class__.__name__
            if cls_name in ["BaseModel", "User", "Place", "State",
                            "Review", "City", "Amenity"]:
                _id = obj.to_dict().get("id", None)
                if _id:
                    key = f"{cls_name}.{_id}"
                    if key in FileStorage.__objects:
                        del FileStorage.__objects[key]
                        self.save()

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = f.read()
                if temp:
                    temp = json.loads(temp)
                    for key, val in temp.items():
                        FileStorage.__objects[key] = classes[
                            val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
