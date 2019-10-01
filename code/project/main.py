import msteering
import time

if __name__ == "__main__":
		print("Start")
		msteering.turnLeft()
		a = 1000
		while True:
			print(msteering.feedback_ADC())
			time.sleep(1)
	