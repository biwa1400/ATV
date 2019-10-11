import msteering
import PID_A
import time
import thread
import numpy as np

def control(input_pid):
	threshold = 0.02
	pwm_scale = 10
	state = False
	
	freq = abs(input_pid)*pwm_scale+50
	
	if (abs(input_pid) < threshold):
		msteering.stop()
		state = True
		return freq,state
	
	if input_pid >= 0:
		msteering.turnLeft()
	else:
		msteering.turnRight()
	
	msteering.ctrlSpeed_PWM(freq)	
	
	return freq,state
	
	
angle = 0.5
def steer(threadName):
	global angle
	kp,ki,kd=(1,0,0)
	incPid = PID_A.IncrementalPID(kp,ki,kd)
	while True:
		adc = msteering.feedback_ADC()
		pid=incPid.step(angle,adc)
		freq,state = control(pid)
		print(state,"%.4f %.4f %.4f" %(adc,pid,freq))
		time.sleep(0.5) 

	

	
if __name__ == "__main__":
		print("Start")
		thread.start_new_thread(steer,(None,))
		while True:
			for i in np.arange(0.2,0.8,0.1):
				print("angle:",i)
				angle = i
				time.sleep(10)

