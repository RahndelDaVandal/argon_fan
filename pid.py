import time

kp: float()
ki: float()
kd: float()
input: float()
output: float()
setpoint: float()
start_time = time.monotonic()
err_sum: float()
last_err: float()
last_time: time.monotonic()
sample_time = 1 #Sec


def compute() -> None:
	now = time()
	time_change = now - last_time

	if time_change >= sample_time:
		error = setpoint - input
		err_sum += error
		d_err = error - last_err

		output = kp * error + ki * err_sum + kd * d_err

		last_err = error
		last_time = now
		
def set_tunings(kp:float(), ki:float(), kd:float()) -> None:
	kp = kp
	ki = float(ki * sample_time)
	kd = float(kd / sample_time)
	
def set_sample_time(new_sample_time:int):
	
	if new_sample_time > 0:
		ratio = new_sample_time / sample_time
		
		ki *= ratio
		kd /= ratio
		sample_time = new_sample_time


