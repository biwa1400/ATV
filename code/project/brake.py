import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM 
import time

PIN_PWM = "P9_14"

def init():
	duty = 10
	freq = 50
	PWM.start(PIN_PWM, duty, freq, polarity=0)
	
def setAngle(value):
	if value >= 0 and value <= 180:
		value = ((value/180.0)*1.7+0.7)/20*100
		print(value)
		PWM.set_duty_cycle(PIN_PWM, value) 
	else:
		raise ValueError('The angle should be setted in 0-180 degress ')


if __name__ == '__main__':
	init()
	while True:
		for i in range(0,180,20):
			setAngle(i)
			time.sleep(5)
	