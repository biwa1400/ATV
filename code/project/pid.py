import matplotlib.pyplot as plt
class IncPID:
	def __init__(self,p,i,d):
		self.Kp = p
		self.Ki = i
		self.Kd = d
		
		self.PIDout = 0.0
		self.out = 0.0
		self.out_1 = 0.0
		
		self.ek = 0.0
		self.ek_1 = 0.0
		self.ek_2 = 0.0
		
	def update(self,value):
		self.error = value - self.out
		increase = self.Kp * (self.ek-self.ek_1) + self.Ki*self.ek + self.Kd*(self.ek-2*ek_1+ek_2)
		self.PIDout += increase
		self.ek_2 = self.ek_1
		self.ek_1 = self.ek
		
	def ineriaTime(self,inertiaTime,sampleTime):
		self.out = (inertiaTime*self.out_1 + sampleTime*self.out)/(inertiaTime+sampleTime)
		self.out_1 = self.out
		
	def getValue(self):
		return self.out
		
if __name__ == "__main__":
	axisX=list()
	axisY=list()
	incP = IncPID(4.5,0.5,0.1)
	for i in range (1,500):
		incP.update(100.2)
		incP.ineriaTime(3,0.1)
		
		axisX.append(i)
		axisY.append(incP.getValue())
		
	plt.figure(1)
	plt.plot(axisX,axisY)
	plt.show()

		