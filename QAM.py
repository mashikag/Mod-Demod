from point import Point	
from LookupTable import LookupTable
import BitStringHelper as BSH
import BitGenerator as BG
import Encoder
import math

LINEAR = 0
GRAY = 1

def createMod2LookupTable():
	table = LookupTable()
	table.add('0', Point(-1,0))
	table.add('1', Point(1,0))
	return table


def modLevels2(bits):
	modList = []
	table = createMod2LookupTable()
	for bit in bits:
		modList.append(table.getSymbol(bit))
	return modList


def demodLevels2(symbols):
	bits = []
	table = createMod2LookupTable()
	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits


# Creates a 2D array with all valid I/Q point
# that can be within it for a pointsPerSide * pointsPerSide
# constellation diagram 
def generatePointsMatrix(pointsPerSide):
	incrementValue = 2 / (float)(pointsPerSide - 1)

	points = []
	qVal = 1
	for i in range(0, pointsPerSide):
		nextRow = []
		iVal = -1
		for j in range(0, pointsPerSide):
			nextRow.append(Point(iVal, qVal))
			iVal += incrementValue
		qVal -= incrementValue
		points.append(nextRow)
	return points


def createMod4LinearLookupTable():
	table = LookupTable()
	values = BG.generateBitList(2)

	stringValues = []
	for value in values:
		stringValues.append(BSH.charListToString(value))
	
	points = generatePointsMatrix(2)
	nextString = 0
	for i in range(0, 2):
		for j in range(0, 2):
			table.add(stringValues[nextString], points[i][j])
			nextString += 1

	return table


def createMod4GrayLookupTable():
	table = LookupTable()
	values = BG.generateBitList(2)

	stringValues = []
	for value in values: 
		stringValues.append(BSH.charListToString(Encoder.convertToGray(value)))

	points = generatePointsMatrix(2)
	nextString = 0
	for i in range(0, 2):
		for j in range(0, 2):
			table.add(stringValues[nextString], points[i][j])
			nextString += 1

	return table


def modLevels4(bits, encoding):
	modList = []
	table = None

	if encoding == LINEAR:
		table = createMod4LinearLookupTable()
	else:
		table = createMod4GrayLookupTable()

	symbols = BSH.divideIntoBitStrings(bits, 2)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)

	return modList


def demodLevels4(symbols, encoding):
	bits = []
	table = None
	if encoding == LINEAR:
		table = createMod4LinearLookupTable()
	else:
		table = createMod4GrayLookupTable()

	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits


def createMod8LookupTable(encoding):
	table = LookupTable()
	values = BG.generateBitList(3)

	stringValues = []
	for value in values: 
		if encoding == LINEAR:
			stringValues.append(BSH.charListToString(value))
		else:
			stringValues.append(BSH.charListToString(Encoder.convertToGray(value)))

	bitMatrix = []

	nextRow = []
	nextRow.append(stringValues[0])
	nextRow.append(stringValues[1])
	nextRow.append(stringValues[2])
	bitMatrix.append(nextRow)

	nextRow = []
	nextRow.insert(0, stringValues[3])
	nextRow.insert(0, None)
	nextRow.insert(0, stringValues[7])
	bitMatrix.append(nextRow)

	nextRow = []
	nextRow.append(stringValues[6])
	nextRow.append(stringValues[5])
	nextRow.append(stringValues[4])
	bitMatrix.append(nextRow)

	points = generatePointsMatrix(3)

	for i in range(0,3):
		for j in range(0,3):
			table.add(bitMatrix[i][j], points[i][j])
			
	return table


def modLevels8(bits, encoding):
	modList = []
	table = createMod8LookupTable(encoding)

	symbols = BSH.divideIntoBitStrings(bits, 3)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)

	return modList


def demodLevels8(symbols, encoding):
	bits = []
	table = None
	table = createMod8LookupTable(encoding)

	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits


# Generates a matrix that is 2^numberOfBits * 2^numberOfBits in size
# and populates it with all possible values between 0 and 2^numberOfBits.
# 
# For linear encoding these values are place in the order they are generated
# with no concern for the number of bits that change between adjacent values. 
#
# For Gray encoding a Karnaugh map is used in order to guarantee that no
# two adjacent values differ by more than a single bit. 
def generateSquareMatrix(numberOfBits, encoding):
	bitsPerSide = int(math.sqrt(2 ** numberOfBits))
	linearList = BG.generateBitList(int(math.log(bitsPerSide,2)))
	grayList = []
	listToUse = linearList
	if encoding == GRAY:
		for value in linearList:
			grayList.append(Encoder.convertToGray(value))
		listToUse = grayList	

	stringList = []
	for value in listToUse:
		stringList.append(BSH.charListToString(value))

	matrix = []
	for i in range(0,bitsPerSide):
		nextRow = []
		for j in range(0, bitsPerSide):
			newValue = stringList[i] + stringList[j]
			nextRow.append(newValue)
		matrix.append(nextRow)
	return matrix


def printSquareMatrix(matrix):
	sideLength = len(matrix[0])

	for i in range (0,sideLength):
		for j in range(0, sideLength):
			print(matrix[i][j]),
		print("\n"),


def createMod16LookupTable(encoding):
	table = LookupTable()

	points = generatePointsMatrix(4)
	bitMatrix = generateSquareMatrix(4, encoding)

	for i in range(0,4):
		for j in range(0,4):
			table.add(bitMatrix[i][j], points[i][j])
			
	return table


def modLevels16(bits, encoding):
	modList = []
	table = createMod16LookupTable(encoding)

	symbols = BSH.divideIntoBitStrings(bits, 4)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)

	return modList


def demodLevels16(symbols, encoding):
	bits = []
	table = createMod16LookupTable(encoding)

	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits


def createMod64LookupTable(encoding):
	table = LookupTable()

	points = generatePointsMatrix(8)
	bitMatrix = generateSquareMatrix(6, encoding)

	for i in range(0, 8):
		for j in range(0, 8):
			table.add(bitMatrix[i][j], points[i][j])

	return table


def modLevels64(bits, encoding):
	modList = []
	table = createMod64LookupTable(encoding)

	symbols = BSH.divideIntoBitStrings(bits, 6)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)

	return modList


def demodLevels64(symbols, encoding):
	bits = []
	table = createMod64LookupTable(encoding)

	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits


def createMod256LookupTable(encoding):
	table = LookupTable()

	points = generatePointsMatrix(16)
	bitMatrix = generateSquareMatrix(8, encoding)

	for i in range(0, 16):
		for j in range(0, 16):
			table.add(bitMatrix[i][j], points[i][j])

	return table


def modLevels256(bits, encoding):
	modList = []
	table = createMod256LookupTable(encoding)

	symbols = BSH.divideIntoBitStrings(bits, 8)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)

	return modList


def demodLevels256(symbols, encoding):
	bits = []
	table = createMod256LookupTable(encoding)

	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits


def createMod1024LookupTable(encoding):
	table = LookupTable()

	points = generatePointsMatrix(32)
	bitMatrix = generateSquareMatrix(10, encoding)

	for i in range(0, 32):
		for j in range(0, 32):
			table.add(bitMatrix[i][j], points[i][j])

	return table


def modLevels1024(bits, encoding):
	modList = []
	table = createMod1024LookupTable(encoding)

	symbols = BSH.divideIntoBitStrings(bits, 10)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)

	return modList


def demodLevels1024(symbols, encoding):
	bits = []
	table = createMod1024LookupTable(encoding)

	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits




# Given a matrix that can be divided equally into 4 quadrants
# this function mirror the values in that quadrant into the other
# three quadrants. 
#
# Eg. The top right quadrant with be mirrored along the y axis and so on
# Each of the 4 quadrant's  value then has one of the four possible 2 bit sequences
# 00,01,10,11 prepended to them. This makes even value in the matrix unique while
# allow the programming of a single quadrant only. 
def mirrorTopLeftQuadrant(matrix):
	quadSize = len(matrix[0]) / 2

	for i in range(0, quadSize):
		count = quadSize
		stack = []
		for j in range(0, quadSize * 2):
			if count > 0:
				stack.append(matrix[i][j])
				count -= 1
			else:
				matrix[i][j] = stack.pop()

	for i in range(0, quadSize * 2):
		count = quadSize
		stack = []
		for j in range(0, quadSize * 2):
			if count > 0:
				stack.append(matrix[j][i])
				count -= 1
			else:
				matrix[j][i] = stack.pop()

	for i in range(0, quadSize * 2):
		for j in range(0, quadSize * 2):
			if matrix[i][j] != None:
				if i < quadSize and j < quadSize:		#00
					matrix[i][j] = "00" + matrix[i][j]
				elif i < quadSize and j >= quadSize:	#01
					matrix[i][j] = "01" + matrix[i][j]
				elif j < quadSize and i >= quadSize:	#10
					matrix[i][j] = "10" + matrix[i][j]
				else:									#11
					matrix[i][j] = "11" + matrix[i][j]


# Generates a skeleton matrix with will hold
# the cross constellation diagram for 32 QAM.
# 
# Points that will not be used are marked as
# None
def generateBaseBitStringMatrixMod32():
	bitStrings = []
	for i in range(0,6):
		nextRow = []
		for j in range(0,6):
			nextRow.append(" ")
		bitStrings.append(nextRow)

	bitStrings[0][0] = None
	bitStrings[0][5] = None
	bitStrings[5][0] = None
	bitStrings[5][5] = None
	return bitStrings


def createMod32LookupTable(encoding):
	table = LookupTable()

	points = generatePointsMatrix(6)
	baseBitStrings = generateBaseBitStringMatrixMod32()
	
	if encoding == LINEAR:
		linearList = BG.generateBitList(5)
		index = 0
		for i in range(0, 6):
			for j in range(0, 6):
				if baseBitStrings[i][j] != None:
					baseBitStrings[i][j] = BSH.charListToString(linearList[index])
					index += 1

	else:
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

		# With QAM levels that are an odd power of 2 it is no longer possible
		# to arrange the values such that no 2 differ by more than 1 bit. The 
		# above pattern is the best that can be done. It gives 8 adjacent pairs
		# that differ by more than 1 bit. This pattern is scaled up to be used 
		# in 128 and 512 QAM. 
		mirrorTopLeftQuadrant(baseBitStrings)

	for i in range(0, 6):
		for j in range(0, 6):
			if baseBitStrings[i][j] != None:
				table.add(baseBitStrings[i][j], points[i][j])	 

	return table


def modLevels32(bits, encoding):
	modList = []
	table = createMod32LookupTable(encoding)

	symbols = BSH.divideIntoBitStrings(bits, 5)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)

	return modList


def demodLevels32(symbols, encoding):
	bits = []
	table = createMod32LookupTable(encoding)

	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits


def generateBaseBitStringMatrixMod128():
	bitStrings = []
	for i in range(0,12):
		nextRow = []
		for j in range(0,12):
			nextRow.append(" ")
		bitStrings.append(nextRow)

	#top left
	for i in range(0,2):
		for j in range(0, 2):
			bitStrings[i][j] = None

	#top right
	for i in range(0,2):
		for j in range(10, 12):
			bitStrings[i][j] = None

	# bottom left
	for i in range(10,12):
		for j in range(0, 2):
			bitStrings[i][j] = None

	# bottom right
	for i in range(10,12):
		for j in range(10, 12):
			bitStrings[i][j] = None

	return bitStrings


def createBlankSquareMatrix(side):
	matrix = []
	for i in range(0, side):
		nextRow = []
		for j in range(0, side):
			nextRow.append('.')
		matrix.append(nextRow)
	return matrix


# Fills a 2x2 square in the passed matrix starting with
# the value in startValue. The first value is entered
# in the bottom left location and the rest are filled in
# in an anti-clockwise direction. 
def bottomLeftFillerMod128(matrix, i, j, startValue):
	matrix[i+1][j] = startValue
	startValue += 1
	matrix[i+1][j+1] = startValue
	startValue += 1
	matrix[i][j+1] = startValue
	startValue += 1
	matrix[i][j] = startValue


# Fills a 2x2 square in the passed matrix starting with
# the value in startValue. The first value is entered
# in the top right location and the rest are filled in
# in an anti-clockwise direction. 
def topRightFillerMod128(matrix, i, j, startValue):
	matrix[i][j+1] = startValue
	startValue += 1
	matrix[i][j] = startValue
	startValue += 1
	matrix[i+1][j] = startValue
	startValue += 1
	matrix[i+1][j+1] = startValue


# Fills a 2x2 square in the passed matrix with Nones. 
def noneFillerMod128(matrix, i, j):
	matrix[i][j] = None
	matrix[i+1][j] = None
	matrix[i][j+1] = None
	matrix[i+1][j+1] = None


# The matrix uses the 32 QAM Gray mapping as a base 
# and fills in the values according to that template.
# Eg. if in the 32 QAM version a 0 was placed in that
# location then in the 128 version the values 0,1,2,3
# are placed in the 4 locations that map to the 
# original 32 Qam location. Rather than filling the
# reference array with the bit sequences, the reference
# array is filled with the decimal number representing 
# the binary value. 
def generateReferenceArrayFor128():
	referenceArray = [[4,3,None], [7,6,5], [0,1,2]]
	matrix = createBlankSquareMatrix(6)

	for i in range(0, 6, 2):
		for j in range(0, 6, 2):
			startValue = referenceArray[i/2][j/2]
			if startValue != None:
				fillerMethod = bottomLeftFillerMod128
				if(j % 4 != 0):
					fillerMethod = topRightFillerMod128

				fillerMethod(matrix, i, j, startValue * 4)
			else:
				noneFillerMod128(matrix, i, j)
	return matrix


# Fills the reference array generated from the 32 QAM
# pattern into the top left quadrant of a full sized
# matrix so that it can be mirrored into the other quadrants 
# as before
def fillInBitStringMatrixMod128(fullMatrix):
	referenceArray = [[4,3,None], [7,6,5], [0,1,2]]
	matrix = generateReferenceArrayFor128()
	reversedMatrix = []
	for i in range(0,6):
		nextRow = []
		for j in range(0,6):
			nextRow.insert(0,matrix[i][j])
		reversedMatrix.append(nextRow)

	for i in range(0, 6):
		for j in range(0,6):
			fullMatrix[i][j] = reversedMatrix[i][j]


# Replaces the index values used in the reference array with
# Gray code values. 
def replaceWithGrayCodeBinary(matrix, numberOfBits):
	bitValues = BG.generateBitList(numberOfBits - 2);
	grayValues = []
	for bitValue in bitValues: 
		grayValues.append(BSH.charListToString(Encoder.convertToGray(bitValue)))

	for i in range(0,12):
		for j in range(0,12):
			if matrix[i][j] != None and matrix[i][j] != ' ':
				matrix[i][j] = grayValues[int(matrix[i][j])]


def createMod128LookupTable(encoding):
	table = LookupTable()

	points = generatePointsMatrix(12)
	baseBitStrings = generateBaseBitStringMatrixMod128()
	
	if encoding == LINEAR:
		linearList = BG.generateBitList(7)
		index = 0
		for i in range(0, 12):
			for j in range(0, 12):
				if baseBitStrings[i][j] != None:
					baseBitStrings[i][j] = BSH.charListToString(linearList[index])
					index += 1

	else:
		fillInBitStringMatrixMod128(baseBitStrings)
		replaceWithGrayCodeBinary(baseBitStrings, 7)
		mirrorTopLeftQuadrant(baseBitStrings)
		
	for i in range(0, 12):
		for j in range(0, 12):
			if baseBitStrings[i][j] != None:
				table.add(baseBitStrings[i][j], points[i][j])	 

	return table


def modLevels128(bits, encoding):
	modList = []
	table = createMod128LookupTable(encoding)

	symbols = BSH.divideIntoBitStrings(bits, 7)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)

	return modList


def demodLevels128(symbols, encoding):
	bits = []
	table = createMod128LookupTable(encoding)

	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits


def generateBaseBitStringMatrixMod512():
	bitStrings = []
	for i in range(0,24):
		nextRow = []
		for j in range(0,24):
			nextRow.append(" ")
		bitStrings.append(nextRow)

	#top left
	for i in range(0,4):
		for j in range(0, 4):
			bitStrings[i][j] = None

	#top right
	for i in range(0,4):
		for j in range(20, 24):
			bitStrings[i][j] = None

	# bottom left
	for i in range(20,24):
		for j in range(0, 4):
			bitStrings[i][j] = None

	# bottom right
	for i in range(20,24):
		for j in range(20, 24):
			bitStrings[i][j] = None

	return bitStrings


# Generates a reference array for 512 based on 128. To see
# how this is done look at the generateReferenceArrayFor128()
# method above which does the same thing but uses QAM 32 as
# a reference. 
def generateReferenceArrayFor512():
	referenceArray = generateReferenceArrayFor128()
	matrix = createBlankSquareMatrix(12)

	for i in range(0, 12, 2):
		for j in range(0, 12, 2):
			startValue = referenceArray[i/2][j/2]
			if startValue != None:
				fillerMethod = bottomLeftFillerMod128
				if(j % 4 != 0):
					fillerMethod = topRightFillerMod128

				fillerMethod(matrix, i, j, startValue * 4)
			else:
				noneFillerMod128(matrix, i, j)
	return matrix

# Copies the reference matrix into the top left
# quadrant of the full matrix
def fillInBitStringMatrixMod512(fullMatrix):
	matrix = generateReferenceArrayFor512()
	reversedMatrix = []
	for i in range(0,12):
		nextRow = []
		for j in range(0,12):
			nextRow.insert(0,matrix[i][j])
		reversedMatrix.append(nextRow)

	for i in range(0, 12):
		for j in range(0,12):
			fullMatrix[i][j] = reversedMatrix[i][j]


def createMod512LookupTable(encoding):
	table = LookupTable()

	points = generatePointsMatrix(24)
	baseBitStrings = generateBaseBitStringMatrixMod512()
	
	if encoding == LINEAR:
		linearList = BG.generateBitList(9)
		index = 0
		for i in range(0, 24):
			for j in range(0, 24):
				if baseBitStrings[i][j] != None:
					baseBitStrings[i][j] = BSH.charListToString(linearList[index])
					index += 1

	else:
		fillInBitStringMatrixMod512(baseBitStrings)
		replaceWithGrayCodeBinary(baseBitStrings, 9)
		mirrorTopLeftQuadrant(baseBitStrings)
		
	for i in range(0, 24):
		for j in range(0, 24):
			if baseBitStrings[i][j] != None:
				table.add(baseBitStrings[i][j], points[i][j])	 

	return table


def modLevels512(bits, encoding):
	modList = []
	table = createMod512LookupTable(encoding)

	symbols = BSH.divideIntoBitStrings(bits, 9)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)

	return modList


def demodLevels512(symbols, encoding):
	bits = []
	table = createMod512LookupTable(encoding)

	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits


def mod(bits, levels, encoding):
	if levels == 2:
		return modLevels2(bits)
	if levels == 4:
		return modLevels4(bits, encoding)
	if levels == 8:
		return modLevels8(bits, encoding)
	if levels == 16:
		return modLevels16(bits, encoding)
	if levels == 32:
		return modLevels32(bits, encoding)
	if levels == 64:
		return modLevels64(bits, encoding)
	if levels == 128:
		return modLevels128(bits, encoding)
	if levels == 256:
		return modLevels256(bits, encoding)
	if levels == 512:
		return modLevels512(bits, encoding)
	if levels == 1024:
		return modLevels1024(bits, encoding)


def demod(symbols, levels, encoding):
	if levels == 2:
		return demodLevels2(symbols)
	if levels == 4:
		return demodLevels4(symbols, encoding)
	if levels == 8:
		return demodLevels8(symbols, encoding)
	if levels == 16:
		return demodLevels16(symbols, encoding)
	if levels == 32:
		return demodLevels32(symbols, encoding)
	if levels == 64:
		return demodLevels64(symbols, encoding)
	if levels == 128:
		return demodLevels128(symbols, encoding)
	if levels == 256:
		return demodLevels256(symbols, encoding)
	if levels == 512:
		return demodLevels512(symbols, encoding)
	if levels == 1024:
		return demodLevels1024(symbols, encoding)
