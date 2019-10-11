import msteering
import pid
import time

def control(input_pid):
	threshold = 0.02
	pwm_scale = 40
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
	

	
if __name__ == "__main__":
		print("Start")
		'''
		msteering.turnLeft()
		a = 1000
		for i in range(1,10):
			a = i*1
			msteering.ctrlSpeed_PWM(a)
			time.sleep(2)
		msteering.stop()
		'''
		kp,ki,kd=(2,0,0)
		incPid = pid.IncrementalPID(kp,ki,kd)
		while True:
			adc = msteering.feedback_ADC()
			pid=incPid.step(0.5,adc)
			freq,state = control(pid)
			print("%.4f %.4f %.4f" %(adc,pid,freq))
			print(state)
			time.sleep(0.5) 
