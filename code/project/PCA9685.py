import time
import math
import smbus
i2c_bus = smbus.SMBus(2) # pins D9 19, 20, /dev/i2c-1

PCA9685_ADDRESS    = 0x40
MODE1              = 0x00
MODE2              = 0x01
SUBADR1            = 0x02
SUBADR2            = 0x03
SUBADR3            = 0x04
PRESCALE           = 0xFE
LED0_ON_L          = 0x06
LED0_ON_H          = 0x07
LED0_OFF_L         = 0x08
LED0_OFF_H         = 0x09
ALL_LED_ON_L       = 0xFA
ALL_LED_ON_H       = 0xFB
ALL_LED_OFF_L      = 0xFC
ALL_LED_OFF_H      = 0xFD

# Bits:
RESTART            = 0x80
SLEEP              = 0x10
ALLCALL            = 0x01
INVRT              = 0x10
OUTDRV             = 0x04

class PCA9685(object):
	def __init__(self, address=PCA9685_ADDRESS, smbus=i2c_bus, **kwargs):
		self._device = i2c_bus
		self.set_all_pwm(0, 0)
		self._device.write_byte_data(PCA9685_ADDRESS,MODE2, OUTDRV)
		self._device.write_byte_data(PCA9685_ADDRESS,MODE1, ALLCALL)
		time.sleep(0.005)  # wait for oscillator
		mode1 = self._device.read_byte_data(PCA9685_ADDRESS,MODE1)
		mode1 = mode1 & ~SLEEP  # wake up (reset sleep)
		self._device.write_byte_data(PCA9685_ADDRESS,MODE1, mode1)
		time.sleep(0.005)  # wait for oscillator
		

	def set_pwm_freq(self, freq_hz):
		"""Set the PWM frequency to the provided value in hertz."""
		prescaleval = 25000000.0    # 25MHz
		prescaleval /= 4096.0       # 12-bit
		prescaleval /= float(freq_hz)
		prescaleval -= 1.0
		prescale = int(math.floor(prescaleval + 0.5))
		oldmode = self._device.read_byte_data(PCA9685_ADDRESS,MODE1);
		newmode = (oldmode & 0x7F) | 0x10    # sleep
		self._device.write_byte_data(PCA9685_ADDRESS,MODE1, newmode)  # go to sleep
		self._device.write_byte_data(PCA9685_ADDRESS,PRESCALE, prescale)
		self._device.write_byte_data(PCA9685_ADDRESS,MODE1, oldmode)
		time.sleep(0.005)
		self._device.write_byte_data(PCA9685_ADDRESS,MODE1, oldmode | 0x80)
	
		
	def set_all_pwm (self, on, off):
		"""Sets all PWM channels."""
		self._device.write_byte_data(PCA9685_ADDRESS,ALL_LED_ON_L, on & 0xFF)
		self._device.write_byte_data(PCA9685_ADDRESS,ALL_LED_ON_H, on >> 8)
		self._device.write_byte_data(PCA9685_ADDRESS,ALL_LED_OFF_L, off & 0xFF)
		self._device.write_byte_data(PCA9685_ADDRESS,ALL_LED_OFF_H, off >> 8)
		
	def set_pwm(self, channel, on, off):
		"""Sets a single PWM channel."""
		self._device.write_byte_data(PCA9685_ADDRESS,LED0_ON_L+4*channel, on & 0xFF)
		self._device.write_byte_data(PCA9685_ADDRESS,LED0_ON_H+4*channel, on >> 8)
		self._device.write_byte_data(PCA9685_ADDRESS,LED0_OFF_L+4*channel, off & 0xFF)
		self._device.write_byte_data(PCA9685_ADDRESS,LED0_OFF_H+4*channel, off >> 8)
		
		
def set_servo_pulse(pwm,channel, pulse):
	pulse_length = 1000000    # 1,000,000 us per second
	pulse_length //= 60       # 60 Hz
	print('{0}us per period'.format(pulse_length))
	pulse_length //= 4096     # 12 bits of resolution
	print('{0}us per bit'.format(pulse_length))
	pulse *= 1000
	pulse //= pulse_length
	pwm.set_pwm(channel, 0, pulse)
	
def test1():
	servo_min = 150  # Min pulse length out of 4096
	servo_max = 600  # Max pulse length out of 4096
	pca = PCA9685()
	pca.set_pwm_freq(60)
	for i in range(150,600,10):
		pca.set_pwm(0, 0, i)
		time.sleep(1)



if __name__ == '__main__':
	test1()
