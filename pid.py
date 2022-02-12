from time import clock, sleep

class PID:
	def __init__(
		self, kp:float(), ki:float(), kd:float()
		):		
			
			self.kp = kp
			self.ki = ki
			self.kd = kd
			self.output : float()
			err_sum : float()
			last_err : float()
			last_time : clock()
			
			def compute(
				self, input:float(), setpoint:float()
				) -> float():
					
					curr_time = clock()
					time_change = clock()
					
					error = setpoint - input
					err_sum += (error * time_change)
					d_err = (error - last_err) / time_change
					
					output = kp * error + ki * err_sum + kd * d_err
					
					last_err = error
					last_time = curr_time
	
input : float()
output : float()
setpoint : float()
start_time = clock()

