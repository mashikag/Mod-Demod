import BitStringHelper

def addAndCarry(bits, pos):
	if(bits[pos] == '0'):
		bits[pos] = '1'
		return 0
	else:
		bits[pos] = '0'
		return 1


def increment(bits):
	newBits = bits[:]
	pos = len(bits) - 1
	carry = addAndCarry(newBits, pos)
	while(carry == 1 and pos >= 0):
		pos = pos - 1
		carry = addAndCarry(newBits, pos)
	return newBits


def generateBitList(numberOfBits):
	bits = []
	count = numberOfBits
	while(count > 0):
		bits.extend('0')
		count = count - 1

	permutations = []
	numberOfPermutations = 2 ** numberOfBits
	for count in range(0, numberOfPermutations):
		permutations.append(bits)
		bits = increment(bits)
	return permutations