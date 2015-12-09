
def divideIntoBitStrings(bitList, bitsPerString):
	bitStrings = []

	for segment in range(0, len(bitList), bitsPerString):
		string = ""
		for bit in range(0, bitsPerString):
			string += bitList[segment + bit]
		bitStrings.append(string)

	return bitStrings
