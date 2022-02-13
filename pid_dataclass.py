# pid.py

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
	_i_term: float() = field(default=0, init=False, repr=False)
	_error: float() = field(default=0, init=False, repr=False)
	
	# MODE CONSTANTS
	MANUAL: int() = field(default=0, repr=False,)
	AUTOMATIC: int() = field(default=1, repr=False)

	# DIRECTION CONSTANTS
	DIRECT: int() = field(default=0, repr=False)
	REVERSE: int() = field(default=1, repr=False)
	
	def __post_init__(self):
		self._start_time = time.monotonic()
		self._last_time = time.monotonic()
		self.set_tunings(self.P, self.I, self.D)
		self.set_output_limits(self.out_min, self.out_max)
		self.set_mode(self.in_auto)
		self.set_direction(self.direction)
		self.set_samples(self.samples)
			
	def set_mode(self, mode):
		new_auto = (mode == self.AUTOMATIC)
		if new_auto:
			if not in_auto:
				self.initialize()
		
	def set_direction(self, direction):
		self.direction = direction
		
	def set_tunings(self, P:float(), I:float(), D:float()):
		if (P<0) or (I<0) or (D<0): return
	 
		self.P = P
		self.I = float(I * self.samples)
		self.D = float(D / self.samples)
		
		if self.direction == self.REVERSE:
			self.P = (0 - self.P)
			self.I = (0 - self.I)
			self.D = (0 - self.D)
		
	def set_samples(self, new_samples:float()):
		if new_samples > 0:
			ratio = new_samples / self.samples
			
			self.I *= ratio
			self.D /= ratio
			self.samples = new_samples
		
	def set_output_limits(self, min:float(), max:float()):
		if min > max: return
	
		self.out_min = min
		self.out_max = max
		
		if self._i_term > self.out_max: 
			self._i_term = self.out_max
		if self._i_term < self.out_min: 
			self._i_term = self.out_min
		
	def initialize():
		last_input = input
		i_term = output
		
		if i_term > out_max: i_term = out_max
		if i_term < out_min: i_term = out_min
	
		
	def compute(self):
		pass	
		

P = 1.0
I = 0.5
D = 0.25
set_point = 50

test = PID(P, I, D, set_point)

print(test)

