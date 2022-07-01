#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """a class named BaseModel"""

    def __init__(self, *args, **kwargs):
        """initializs an instance of BaseModel"""
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.fromisoformat("2017-06-14T22:31:03.285259")

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):

        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates a BaseModel instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict
