'''
import matplotlib.pyplot as plt
'''

# IncrementalPID
class IncrementalPID:
	def __init__(self,p,i,d):
		self.Kp = p
		self.Ki = i
		self.Kd = d
		
		self.PIDout = 0.0
		
		self.ek = 0.0
		self.ek_1 = 0.0
		self.ek_2 = 0.0
		
	def step(self,aim,real):
		self.ek = aim - real
		increase = self.Kp * (self.ek-self.ek_1) + self.Ki*self.ek + self.Kd*(self.ek-2*self.ek_1+self.ek_2)
		self.PIDout += increase
		self.ek_2 = self.ek_1
		self.ek_1 = self.ek
		return self.PIDout
		
		
class PositionalPID:
	def __init__(self,p,i,d):
		self.Kp = p
		self.Ki = i
		self.Kd = d
		
		self.PIDout = 0.0
		
		self.ek_1 = 0.0
		self.e_assum = 0.0

		
	def step(self,aim):
		err = aim - self.PIDout
		kp = self.Kp * err
		ki = self.Ki * self.e_assum
		kd = self.Kd * (err - self.ek_1)
		
		self.PIDout = kp+ki+kd
		self.e_assum += err
		self.ek_1 = err
		return self.PIDout
		
		
class InertialSys_PositionalPID(PositionalPID):
	out = 0.0
	out_1 = 0.0

	def __init__(self,p,i,d,inertiaTime,sampleTime):
		super().__init__(p,i,d)
		self.inertiaTime=inertiaTime
		self.sampleTime = sampleTime
		
	def step(self,aim):
		pidOut = super().step(aim)
		self.out = (self.inertiaTime*self.out_1 + self.sampleTime*pidOut)/(self.inertiaTime+self.sampleTime)
		self.out_1 = self.out
		return self.out
		
class InertialSys_IncrementalPID(IncrementalPID):
	out = 0.0
	out_1 = 0.0

	def __init__(self,p,i,d,inertiaTime,sampleTime):
		super().__init__(p,i,d)
		self.inertiaTime=inertiaTime
		self.sampleTime = sampleTime
		
	def step(self,aim):
		pidOut = super().step(aim)
		self.out = (self.inertiaTime*self.out_1 + self.sampleTime*pidOut)/(self.inertiaTime+self.sampleTime)
		self.out_1 = self.out
		return self.out

'''
def test1():
	axisX=list()
	axisY=list()
	

	inertialSys = InertialSys_PositionalPID(1,0.5,0.1,3,0.1)
	for i in range (1,1000):
		value = inertialSys.step(100.2)
		
		axisX.append(i)
		axisY.append(value)
		
	plt.figure(1)
	plt.plot(axisX,axisY)
	plt.show()
	
if __name__ == "__main__":
	test1()
'''
		