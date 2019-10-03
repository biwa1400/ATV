import msteering
import pid
import time

def control(input_pid):
	threshold = 0.02
	pwm_scale = 100
	
	freq = abs(input_pid)*pwm_scale
	
	if (abs(input_pid) < threshold):
		msteering.stop()
		return freq
	
	if input_pid >= 0:
		msteering.turnLeft()
	else:
		msteering.turnRight()
	
	msteering.ctrlSpeed_PWM(freq)	
	
	return freq
	

	
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
			freq = control(pid)
			print("%.4f %.4f %.4f" %(adc,pid,freq))
			

			
			time.sleep(0.5) 
