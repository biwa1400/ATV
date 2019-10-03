import da.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM 
import Adafruit_BBIO.ADC as ADC

PIN_IN_A = "P8_17"
PIN_IN_B = "P8_15"
PIN_PWM = "P8_19"
PIN_ADC = "P9_36"

# PWM frequency 0-10k

def init():
	GPIO.setup(PIN_IN_A, GPIO.OUT)
	GPIO.setup(PIN_IN_B, GPIO.OUT)
	PWM.start(PIN_PWM, 50, 2000, polarity=0)
	ADC.setup()
	
def stop():
	GPIO.output(PIN_IN_A, GPIO.LOW)
	GPIO.output(PIN_IN_B, GPIO.LOW)
	
def turnLeft():
	GPIO.output(PIN_IN_A, GPIO.HIGH)
	GPIO.output(PIN_IN_B, GPIO.LOW)
	
def turnRight():
	GPIO.output(PIN_IN_A, GPIO.LOW)
	GPIO.output(PIN_IN_B, GPIO.HIGH)

def ctrlSpeed_PWM(freq):
	if freq >= 0 and freq <= 10e3:
		PWM.set_frequency(PIN_PWM, freq)
	else:
		raise ValueError('The PWM frequency should be setted in 0-10KHz ')

def feedback_ADC():
	return ADC.read(PIN_ADC)

def release():
	PWM.stop(PIN_PWM)
	PWM.cleanup()


init()
