
def xor(bit1, bit2):
	if(bit1 == bit2):
		return '0'
	else:
		return '1'

def convertToGray(bits):
	length = len(bits)
	output = [bits[0]]
	for pos in range(0, len(bits) - 1):
		output.extend(xor(bits[pos], bits[pos + 1]))
	return output