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


# Place all points to be used in a constellation
# diagram of size pointePerSide * pointsPerside
# in a matrix in their correct location
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

# Places all possible bits string in a matrix of 
# size pointsPerSide * pointsPerSide in the position
# the position they will appear in constellation diagram
def generateSquareBitStringsMatrix(pointsPerSide, bitStrings):
	bitMatrix = []
	index = 0
	forwards = True
	for i in range(0, pointsPerSide):
		nextRow = []
		for j in range(0, pointsPerSide):
			if(forwards):
				nextRow.append(bitStrings[index])
			else:
				nextRow.insert(0, bitStrings[index])
			index = index + 1
		forwards = not forwards
		bitMatrix.append(nextRow)
	return bitMatrix




def createMod4LinearLookupTable():
	table = LookupTable()
	values = BG.generateBitList(2)

	stringValues = []
	for value in values:
		stringValues.append(BSH.charListToString(value))
	
	points = generatePointsMatrix(2)
	bitStrings = generateSquareBitStringsMatrix(2, stringValues)

	for i in range(0, 2):
		for j in range(0, 2):
			table.add(bitStrings[i][j], points[i][j])

	return table
def createMod4GrayLookupTable():
	table = LookupTable()
	values = BG.generateBitList(2)

	stringValues = []
	for value in values: 
		stringValues.append(BSH.charListToString(Encoder.convertToGray(value)))

	points = generatePointsMatrix(2)
	bitStrings = generateSquareBitStringsMatrix(2, stringValues)

	for i in range(0, 2):
		for j in range(0, 2):
			table.add(bitStrings[i][j], points[i][j])

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





def mod(bits, levels, encoding):
	if levels == 2:
		return modLevels2(bits)
	if levels == 4:
		return modLevels4(bits, encoding)
	if levels == 8:
		return modLevels8(bits, encoding)
	if levels == 16:
		return modLevels16(bits, encoding)
	if levels == 64:
		return modLevels64(bits, encoding)
	if levels == 256:
		return modLevels256(bits, encoding)
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
	if levels == 64:
		return demodLevels64(symbols, encoding)
	if levels == 256:
		return demodLevels256(symbols, encoding)
	if levels == 1024:
		return demodLevels1024(symbols, encoding)
