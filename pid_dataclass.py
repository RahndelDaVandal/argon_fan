import time
from dataclasses import dataclass, field

@dataclass
class PID:
	# REQUIRED
	P: float()
	I: float()
	D: float()
	set_point: float()
	
	# DEFAULTS
	samples: float() = 1.0
	out_min: float() = 0
	out_max: float() = 100
	direction: bool() = True
	in_auto: bool() = False
	
	# PRIVATE
	_start_time: float() = field(init=False, repr=False)
	_last_time: float() = field(init=False, repr=False)
	_last_input: float() = field(init=False, repr=False)
	_i_term: float() = field(init=False, repr=False)
	_error: float() = field(init=False, repr=False)
	
	def __post_init__(self):
		self._start_time = time.monotonic()
		self._last_time = time.monotonic()
		self.set_tunings(self.P, self.I, self.D)
		self.set_output_limits(self.out_min, self.out_max)
		self.set_mode(self.in_auto)
		self.set_direction(self.direction)
		self.set_samples(self.samples)
			
	def set_mode(self, mode):
		pass
		
	def set_direction(self, direction):
		pass
		
	def set_tunings(self, P:float(), I:float(), D:float()):
		pass
		
	def set_samples(self, samples:float()):
		pass
		
	def set_output_limits(self, min:float(), max:float()):
		pass
		
	def initialize():
		pass
		
	def compute(self):
		pass	
