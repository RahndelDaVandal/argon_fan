# controller.py

from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod
    def run(self, feedback:float(), setpoint:float()):
        pass

class PID(Controller):
    def run(self, feedback:float(), setpoint:float()):
        pass

class Bang_Bang(Controller):
    def run(self, feedback:float(), setpoint:float()):
        pass
