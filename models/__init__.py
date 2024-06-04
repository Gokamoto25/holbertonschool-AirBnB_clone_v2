#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

# Import the necessary storage classes
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Check the storage type specified in the environment variable
storage_type = getenv('HBNB_TYPE_STORAGE')

# Instantiate the appropriate storage class
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload the storage
storage.reload()
