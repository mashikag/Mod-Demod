
def divideIntoBitStrings(bitList, bitsPerString):
	bitStrings = []

	for segment in range(0, len(bitList), bitsPerString):
		string = ""
		for bit in range(0, bitsPerString):
			string += bitList[segment + bit]
		bitStrings.append(string)

	return bitStrings

def stringToCharList(string):
	chars = []
	for char in string: 
		chars.append(char)
	return chars

def charListToString(charList):
	string = ""
	for char in charList:
		string += char
	return string
