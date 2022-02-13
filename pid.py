import time

kp: float() #
ki: float() #
kd: float() #
input: float()
output: float()
setpoint: float() #
start_time = time.monotonic() #
#err_sum: float()
#last_err: float()
last_time: time.monotonic() #
sample_time = 1 #Sec #
last_input: float() #
i_term : float() #
out_max : float() #
out_min : float() #
in_auto = False #

MANUAL = 0 #
AUTOMATIC = 1 #

DIRECT = 0 #
REVERSE = 1 #
control_direction = DIRECT #

def compute() -> None:
	if not in_auto: return
	
	now = time()
	time_change = now - last_time

	if time_change >= sample_time:
		error = setpoint - input
		i_term += ki * error
		if i_term >= out_max: i_term = out_max
		if i_term <= out_min: i_term = out_min
		d_input = (input - last_input)

		output = kp * error + i_term - kd * d_input
		if output > out_max: output = out_max
		if output < out_min: output = out_min

		last_input = input
		last_time = now
		
def set_tunings(kp:float(), ki:float(), kd:float()) -> None:
	if (p<0) or (i<0) or (d<0): return
	 
	kp = kp
	ki = float(ki * sample_time)
	kd = float(kd / sample_time)
	
	if control_direction == REVERSE:
		kp = (0 - kp)
		ki = (0 - ki)
		kd = (0 - kd)
	
def set_sample_time(new_sample_time:int):
	
	if new_sample_time > 0:
		ratio = new_sample_time / sample_time
		
		ki *= ratio
		kd /= ratio
		sample_time = new_sample_time
		
def set_output_limits(min:float(), max:float()):
	if min > max: return
	
	out_min = min
	out_max = max
	
	if output > out_max: output = out_max
	if output < out_min: output = out_min
	
	if i_term > out_max: i_term = out_max
	if i_term < out_min: i_term = out_min
	
def set_mode(mode:int()):
	new_auto = (mode == AUTOMATIC)
	if new_auto:
		if not in_auto:
			initialize()
			
	in_auto = new_auto
	
def initialize():
	last_input = input
	i_term = output
	
	if i_term > out_max: i_term = out_max
	if i_term < out_min: i_term = out_min
	
def set_control_direction(direction: int):
	control_direction = direction


