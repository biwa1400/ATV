import smbus
bus1 = smbus.SMBus(2) # pins D9 19, 20, /dev/i2c-1
tmp102_addr = 0x40
data = bus1.read_byte_data(tmp102_addr, 0xfb)
print(data)

class Servo:
	def __init__(self,smbus):
		self.i2c = smbus
	def 