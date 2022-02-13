# Class refactor for pid.py
import time
from random import randint
import matplotlib.pyplot as plt
import numpy as np


class PID:
	def __init__(self,
														P: float(),
														I: float(),
														D: float(),
														set_point: float(),
														out_min: float()=0,
														out_max: float()=100,
														sample_time: int()=1,
														control_direction: bool()=True,
														in_auto: bool()=False,
														*kwargs):
		self.P = P
		self.I = I
		self.D = D
		self.set_point = set_point
		self.sample_time = sample_time
		self.out_min = out_min
		self.out_max = out_max
		self.control_direction = control_direction
		self.in_auto = in_auto

		self._start_time = time.monotonic()
		self._last_time = time.monotonic()
		self._last_input = 0.0
		self._i_term = 0.0
		self._error: float()

		# Constants for setting in_auto
		MANUAL = 0
		AUTOMATIC = 1

		# Constants for setting control_direction
		DIRECT = 0
		REVERSE = 1

	def compute(self, input: float()) -> float():
		if not self.in_auto:
			return 0.0

		now = time.monotonic()
		time_change = now - self._last_time

		if time_change >= self.sample_time:
			self._error = self.set_point - input
			self._i_term += self.I * self._error
			if self._i_term >= self.out_max: self.i_term = self.out_max
			if self._i_term <= self.out_min: self._i_term = self.out_min
			d_input = (input - self._last_input)

			output = self.P * self._error + self._i_term - self.D * d_input
			if output > self.out_max: output = self.out_max
			if output < self.out_min: output = self.out_min

			self.last_input = input
			self.last_time = now

			if output == None:
				print("output = None")
				return 0.0
			else:
				return output
				
	def _configure(self):


output = 0

pid = PID(P=.6, I=0.08, D=0.002, set_point=80, in_auto=True, sample_time=0.25)

output = 0.0

input = 80

data = []
print(f'P: {pid.P} I: {pid.I} D: {pid.D}')
print(f'Set Point = {pid.set_point}')

t = 0
x = np.empty(0)
f = np.empty(0)
o = np.empty(0)
s = np.empty(0)
o_std = np.empty(0)

rate = -20

for i in range(0, 100):
	input += (randint(-7, 2) + rate)
	output = pid.compute(input)
	if output == None:
		output = 0.0
	new_input = input + output
	input = new_input
	t += 1
	x = np.append(t, x)
	f = np.append(input, f)
	o = np.append(output, o)
	curr_o_std = np.std(o)
	o_std = np.append(curr_o_std, o_std)
	s = np.append(pid.set_point, s)
	print(f'feedback: {input:.2f} output: {output:.2f} STD: {curr_o_std:.2f} DfS: {input - pid.set_point:.2f}')
	time.sleep(pid.sample_time)

print(x)

plt.plot(x, s, label='Set Point', color='b', linestyle='--')
plt.plot(x, f, label='Feedback', color='r')
plt.plot(x, o, label='Output', color='g')
plt.title(f'P:{pid.P} I:{pid.I} D:{pid.D} STD:{np.std(o):.2f}')

#plt.legend()

plt.tight_layout()
plt.show()
#with open('output.txt', 'w') as outfile:
#outfile.write(str(data))

#plt.plot(x,y, color='r')
#plt.savefig('output.png')
#plt.show()

