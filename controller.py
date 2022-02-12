# controller.py

from abc import ABC, abstractmethod

class Controller(ABC):
	@abstractmethod
	def __init__(self, *kwargs):
		pass

	@abstractmethod
	def run(self, feedback:float(), setpoint:float()):
		pass
		
class PID(Controller):
	def __init__(self, *kwargs):
		pass
	
	def run(self, feedback:float(), setpoint:float()):
		pass
		
class Bang_Bang(Controller):
	def __init__(self, *kwargs):
		pass
		
	def run(self, feedback:float(), setpoint:float()):
		pass

