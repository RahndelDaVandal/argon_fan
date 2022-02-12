# controller.py

from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod
    def run(self):
        pass

class PID(Controller):
    def run(self):
        pass

class Bang_Bang(Controller):
    def run(self):
        pass
