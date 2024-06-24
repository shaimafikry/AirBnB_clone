#!/usr/bin/python3
"""init file which will run whenever you run your programm"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
