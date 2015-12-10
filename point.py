import math

class Point: 
	def __init__(self, i, q):
		self.i = i
		self.q = q

	def toString(self):
		return '[I:{},Q:{}]'.format(self.i, self.q)

	def distance(self, point):
		diffXSq = (self.i - point.i) * (self.i - point.i)
		diffYSq = (self.q - point.q) * (self.q - point.q)

		dist = math.sqrt(diffYSq + diffXSq)
		return dist