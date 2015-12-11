from LookupEntry import LookupEntry
from point import Point

class LookupTable:
	def __init__(self):
		self.entries = []


	def stringToCharList(self,string):
		chars = []
		for char in string: 
			chars.append(char)
		return chars

	def add(self,string, point):
		newEntry = LookupEntry(string, point)
		self.entries.append(newEntry)


	def getBestMatchingBitSequence(self,point):
		indexOfBestMatch = 0
		smallestDistanceEncountered = point.distance(self.entries[0].point)

		for nextPoint in range(1, len(self.entries)):
			nextDistance = point.distance(self.entries[nextPoint].point)
			if nextDistance < smallestDistanceEncountered:
				smallestDistanceEncountered = nextDistance
				indexOfBestMatch = nextPoint

		bitStringToReturn = self.entries[indexOfBestMatch].bits
		return self.stringToCharList(bitStringToReturn) 


	def getSymbol(self,bitString):
		for entry in self.entries:
			if(entry.bits == bitString):
				return entry.point

	def toString(self):
		output = ""
		for entry in self.entries:
			output += "{} => {}".format(entry.bits, entry.point.toString())
			output += "\n"
		output += "SIZE: {}".format(len(self.entries))
		return output