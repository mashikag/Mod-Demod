import Modulation
import QAM
import BitStringHelper as BSH
import BitGenerator as BG
import Encoder


def testQAM(numberOfBits, numberOfLevels, encoding):
	failures = 0
	values = BG.generateBitList(numberOfBits)

	encString = "Linear"
	if encoding == 1:
		encString = "Gray"

	print "\n{} QAM {} - number of permutations to test: {}".format(numberOfLevels, encString,len(values))
	for value in values: 
		mod = Modulation.mod(value, Modulation.MOD_SCHEME_QAM,numberOfLevels, encoding)
		demod = Modulation.demod(mod, Modulation.MOD_SCHEME_QAM,numberOfLevels, encoding)
		#print value, " = ", demod
		if value != demod:
			failures += 1
	print "{} QAM {} failures: {}\n".format(numberOfLevels,encString,failures)

def testPSK(numberOfBits, numberOfLevels, encoding):
	failures = 0
	values = BG.generateBitList(numberOfBits)

	encString = "Linear"
	if encoding == 1:
		encString = "Gray"

	print "\n{} PSK {} - number of permutations to test: {}".format(numberOfLevels, encString,len(values))
	for value in values: 
		mod = Modulation.mod(value, Modulation.MOD_SCHEME_PSK,numberOfLevels, encoding)
		demod = Modulation.demod(mod, Modulation.MOD_SCHEME_PSK,numberOfLevels, encoding)
		#print value, " = ", demod
		if value != demod:
			failures += 1
	print "{} PSK {} failures: {}\n".format(numberOfLevels,encString,failures)




# Testing 2-QAM
testQAM(1,2,0)

# Testing 4-QAM Linear
testQAM(2,4,0)
# Testing 4-QAM Gray
testQAM(2,4,1)

# 8 QAM Linear
testQAM(3,8,0)
# 8 QAM Gary
testQAM(3,8,1)

# 16 QAM Linear
testQAM(4,16,0)
# 16 QAM Gray
testQAM(4,16,1)

# 64 QAM Linear
testQAM(6,64,0)
# 64 QAM Gray
testQAM(6,64,1)

# 256 QAM Linear
testQAM(8,256,0)
# 256 QAM Gray
testQAM(8,256,1)

# 1024 QAM Linear
testQAM(10,1024,0)
# 1024 QAM Gray
testQAM(10,1024,1)

# 32 QAM Linear
testQAM(5,32,0)
# 32 QAM Gray
testQAM(5,32,1)

# 128 QAM Linear
testQAM(7,128,0)
# 128 QAM Gray
testQAM(7,128,1)

# 512 QAM Linear
testQAM(9,512,0)
# 128 QAM Gray
testQAM(9,512,1)




# 2 PSK
testPSK(1,2,0)

# 4 PSK Linear
testPSK(2, 4, 0)
# 4 PSK Gray
testPSK(2,4,1)

# 8 PSK Linear
testPSK(3,8,0)
# 8 PSK Gray
testPSK(3,8,1)






# Returns the number of character that differ between strA and strB
def compareStrings(strA, strB):
	listA = BSH.stringToCharList(strA)
	listB = BSH.stringToCharList(strB)

	numberOfDifferences = 0
	for i in range(0, len(listA)):
		if listA[i] != listB[i]:
			numberOfDifferences += 1

	return numberOfDifferences

# Tests to see how many adjacent values differ by more than 1 bit
def differByOneByOnly(array):
	size = len(array[0])

	connectionsChecked = 0
	numberThatDoNoDifferByOneBit = 0
	for i in range(0, size):
		for j in range(0, size):
			if array[i][j] != None:
				if j < size-1:
					if array[i][j + 1] != None:
						connectionsChecked += 1
						diffs = compareStrings(array[i][j], array[i][j + 1])
						if diffs != 1:
							numberThatDoNoDifferByOneBit += 1
				if i < size-1:
					if array[i + 1][j] != None:
						connectionsChecked += 1
						diffs = compareStrings(array[i][j], array[i + 1][j])
						if diffs != 1:
							numberThatDoNoDifferByOneBit += 1

	print "Number that do not differ by a single bit: {}".format(numberThatDoNoDifferByOneBit)
	print "Number of connections checked: {}".format(connectionsChecked)





print "16 QAM Linear"
array = QAM.generateSquareMatrix(4, 0)
differByOneByOnly(array)
print "\n\n"


print "16 QAM Gray"
array = QAM.generateSquareMatrix(4, 1)
differByOneByOnly(array)
print "\n\n"


print "64 QAM Linear"
array = QAM.generateSquareMatrix(6, 0)
differByOneByOnly(array)
print "\n\n"


print "64 QAM Gray"
array = QAM.generateSquareMatrix(6, 1)
differByOneByOnly(array)
print "\n\n"


print "256 QAM Linear"
array = QAM.generateSquareMatrix(8, 0)
differByOneByOnly(array)
print "\n\n"


print "256 QAM Gray"
array = QAM.generateSquareMatrix(8, 1)
differByOneByOnly(array)
print "\n\n"


print "1024 QAM Linear"
array = QAM.generateSquareMatrix(10, 0)
differByOneByOnly(array)
print "\n\n"


print "1024 QAM Gray"
array = QAM.generateSquareMatrix(10, 1)
differByOneByOnly(array)
print "\n\n"




# 32 QAM Linear
baseBitStrings = QAM.generateBaseBitStringMatrixMod32()
linearList = BG.generateBitList(5)
index = 0
for i in range(0, 6):
	for j in range(0, 6):
		if baseBitStrings[i][j] != None:
			baseBitStrings[i][j] = BSH.charListToString(linearList[index])
			index += 1

print "32 QAM Linear"
differByOneByOnly(baseBitStrings)
print "\n\n"


# 32 QAM Gray 
linearList = BG.generateBitList(3)
grayList = []
for value in linearList:
	grayList.append(BSH.charListToString(Encoder.convertToGray(value)))

baseBitStrings[0][0] = None
baseBitStrings[0][1] = grayList[4]
baseBitStrings[0][2] = grayList[3]
baseBitStrings[1][0] = grayList[5]
baseBitStrings[1][1] = grayList[6]
baseBitStrings[1][2] = grayList[7]
baseBitStrings[2][0] = grayList[2]
baseBitStrings[2][1] = grayList[1]
baseBitStrings[2][2] = grayList[0]

QAM.mirrorTopLeftQuadrant(baseBitStrings)

print "32 QAM Gray"
differByOneByOnly(baseBitStrings)
print "\n\n"






# 128 QAM Linear
baseBitStrings = QAM.generateBaseBitStringMatrixMod128()
	
linearList = BG.generateBitList(7)
index = 0
for i in range(0, 12):
	for j in range(0, 12):
		if baseBitStrings[i][j] != None:
			baseBitStrings[i][j] = BSH.charListToString(linearList[index])
			index += 1

print "128 QAM Linear"
differByOneByOnly(baseBitStrings)
print "\n\n"


# 128 QAM Gray 
baseBitStrings = QAM.generateBaseBitStringMatrixMod128()
QAM.fillInBitStringMatrixMod128(baseBitStrings)
QAM.replaceWithGrayCodeBinary(baseBitStrings, 7)
QAM.mirrorTopLeftQuadrant(baseBitStrings)
		
print "128 QAM Gray"
differByOneByOnly(baseBitStrings)
print "\n\n"



# 512 QAM Linear
baseBitStrings = QAM.generateBaseBitStringMatrixMod512()
linearList = BG.generateBitList(9)
index = 0
for i in range(0, 24):
	for j in range(0, 24):
		if baseBitStrings[i][j] != None:
			baseBitStrings[i][j] = BSH.charListToString(linearList[index])
			index += 1

print "512 QAM Linear"
differByOneByOnly(baseBitStrings)
print "\n\n"



# 512 QAM Gray
baseBitStrings = QAM.generateBaseBitStringMatrixMod512()
QAM.fillInBitStringMatrixMod512(baseBitStrings)
QAM.replaceWithGrayCodeBinary(baseBitStrings, 9)
QAM.mirrorTopLeftQuadrant(baseBitStrings)

print "512 QAM Gray"
differByOneByOnly(baseBitStrings)
print "\n\n"