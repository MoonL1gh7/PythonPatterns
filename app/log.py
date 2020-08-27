from patterns.singletons import SingletonsByName
import time
from datetime import datetime


class Logger(metaclass=SingletonsByName):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        print('log--->', text)
