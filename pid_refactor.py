# Class refactor for pid.py
import time
from random import randint
import matplotlib.pyplot as plt


class PID:
	def __init__(self,
														P: float(),
														I: float(),
														D: float(),
														set_point: float(),
														out_min: float()=0,
														out_max: float()=100,
														sample_time: int()=1,
														control_direction: bool()=False,
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


output = 0

pid = PID(P=0.25, I=1, D=0.25, set_point=50, in_auto=True, sample_time=0.5)

output = 0.0

input = 50.0

data = []
print(f'P: {pid.P} I: {pid.I} D: {pid.D}')
print(f'Set Point = {pid.set_point}')

t = 0
x = []
f = []
o = []
s = []

for i in range(0, 1000):
	input += randint(-15, 1)
	output = pid.compute(input)
	if output == None:
		output = 0.0
	new_input = input + output
	input = new_input
	print(f'feedback: {input:.2f} output: {output:.2f}')
	t += 1
	x.append(t)
	f.append(input)
	o.append(output)
	s.append(pid.set_point)
	time.sleep(pid.sample_time)

print()

plt.plot(x, s, label='Set Point', color='b', linestyle='--')
plt.plot(x, f, label='Feedback', color='r')
plt.plot(x, o, label='Output', color='g')
plt.title(f'P:{pid.P} I:{pid.I} D:{pid.D}')

#plt.legend()

plt.tight_layout()
plt.show()
#with open('output.txt', 'w') as outfile:
#outfile.write(str(data))

#plt.plot(x,y, color='r')
#plt.savefig('output.png')
#plt.show()

