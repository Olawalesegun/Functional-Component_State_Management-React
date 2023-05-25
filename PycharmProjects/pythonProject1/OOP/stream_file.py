# Py Thursday 25,05,2023
from abc import abstractmethod, ABC


class InvalidOperationError(Exception):
    pass


class Stream(ABC):

    def __init__(self):
        self.is_open = None

    def open(self):
        if self.is_ooen:
            raise InvalidOperationError("Invalid operation, cannot open")
        self.is_open = True

    @abstractmethod
    def write(self):
        pass


class NetworkStream(Stream, ABC):
    def read(self):
        print("Reading data from a network...")

    def write(self):
        print("")


class MemoryStream():
    def read(self):
        print("Reading data from a network")

    def write(self):
        print("")


