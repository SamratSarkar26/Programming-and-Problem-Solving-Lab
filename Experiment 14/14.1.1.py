 class Complex:
	def initComplex(self):
		self.real , self.img = map(int,input().split())
	def sum(self,c1,c2):
		self.real = c1.real + c2.real
		self.img = c1.img + c2.img
	def display(self):
		if self.img >= 0:
			print(f"{self.real} + {self.img}i")
		else:
			print(f"{self.real} - {abs(self.img)}i")
# Create three instances
c1 = Complex()
c2 = Complex()
c3 = Complex()

# Initialize two complex numbers
c1.initComplex()
c2.initComplex()

# Compute and display sum
c3.sum(c1, c2)
c3.display()
