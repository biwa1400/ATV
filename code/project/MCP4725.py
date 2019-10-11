import smbus
import time
import numpy as np

i2c_bus = smbus.SMBus(2) # pins D9 19, 20, /dev/i2c-2
MCP4275_ADDRESS          = 0x60
MCP4726_CMD_WRITEDAC     = 0x40


class MCP4725:
	def __init__(self,address=MCP4275_ADDRESS,smbus=i2c_bus):
		self._device=i2c_bus
		self._address = address
		
	def setVoltage(self,value):
		value = value * 4096/3.3
	
		bytes =[0,0]
		bytes[0] = int(value/16)
		bytes[1] = int(value%16)<<4
		
		self._device .write_i2c_block_data(self._address,MCP4726_CMD_WRITEDAC,bytes)
		



if __name__ == "__main__":
	print("hello world")
	dac = MCP4725()
	while True:
		for i in np.arange (0,3.3,0.5):
			dac.setVoltage(i)
			time.sleep(1)