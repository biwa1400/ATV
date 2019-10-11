import Adafruit_BBIO.GPIO as GPIO

PIN_INVERT_CONTROL = "P8_11"

def init():
	GPIO.setup(PIN_INVERT_CONTROL, GPIO.OUT)

def front():
	GPIO.output(PIN_INVERT_CONTROL, GPIO.HIGH)
	
def back():
	GPIO.output(PIN_INVERT_CONTROL, GPIO.LOW)
	
	
init()
if __name__ == "__main__":
	front()