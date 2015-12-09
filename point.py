class Point: 
	def __init__(self, i, q):
		self.i = i
		self.q = q

	def toString(self):
		return '[I:{},Q:{}]'.format(self.i, self.q)