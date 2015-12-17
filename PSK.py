from point import Point	
from LookupTable import LookupTable
import BitStringHelper as BSH

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


def createMod4LinearLookupTable():
	table = LookupTable()
	table.add("00", Point(-1,0))
	table.add("01", Point(0, 1))
	table.add("10", Point(1,0))
	table.add("11", Point(0,-1))
	return table


def createMod4GrayLookupTable():
	table = LookupTable()
	table.add("00", Point(1,0))
	table.add("01", Point(0,1))
	table.add("11", Point(-1,0))
	table.add("10",Point(0,-1))
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


def createMod8LinearLookupTable():
	table = LookupTable()
	table.add('000', Point(1,0))
	table.add('001', Point(0.7071, 0.7071))
	table.add('010', Point(0, 1))
	table.add('011', Point(-0.7071, 0.7071))
	table.add('100', Point(-1, 0))
	table.add('101', Point(-0.7071, -0.7071))
	table.add('110', Point(0, -1))
	table.add('111', Point(0.7071, -0.7071))
	return table


def createMod8GrayLookupTable():
	table = LookupTable()
	table.add("000", Point(1,0))
	table.add("001", Point(0.7071, 0.7071))
	table.add("101", Point(0, 1))
	table.add("100", Point(-0.7071, 0.7071))
	table.add("110", Point(-1, 0))
	table.add("111", Point(-0.7071, -0.7071))
	table.add("011", Point(0,-1))
	table.add("010", Point(0.7071, -0.7071))
	return table


def modLevels8(bits, encoding):
	modList = []
	table = None
	if encoding == LINEAR:
		table = createMod8LinearLookupTable()
	else:
		table = createMod8GrayLookupTable()

	symbols = BSH.divideIntoBitStrings(bits, 3)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)
	return modList


def createMod16LinearLookupTable():
	table = LookupTable()
	table.add('0000', Point(1,0))
	table.add('0001', Point(0.9239,0.3827))
	table.add('0010', Point(0.7071,0.7071))
	table.add('0011', Point(0.3827,0.9239))
	table.add('0100', Point(0,1))
	table.add('0101', Point(-0.3827,0.9239))
	table.add('0110', Point(-0.7071,0.7071))
	table.add('0111', Point(-0.9239,0.3827))
	table.add('1000', Point(-1,0))
	table.add('1001', Point(-0.9239,-0.3827))
	table.add('1010', Point(-0.7071,-0.7071))
	table.add('1011', Point(-0.3827,-0.9239))
	table.add('1100', Point(0,-1))
	table.add('1101', Point(0.3827,-0.9239))
	table.add('1110', Point(0.7071,-0.7071))
	table.add('1111', Point(0.9239,-0.3827))
	return table

def createMod16GrayLookupTable():
	table = LookupTable()
	table.add('0000', Point(1,0))
	table.add('0001', Point(0.9239,0.3827))
	table.add('0011', Point(0.7071,0.7071))
	table.add('0010', Point(0.3827,0.9239))
	table.add('0110', Point(0,1))
	table.add('0111', Point(-0.3827,0.9239))
	table.add('0101', Point(-0.7071,0.7071))
	table.add('0100', Point(-0.9239,0.3827))
	table.add('1100', Point(-1,0))
	table.add('1101', Point(-0.9239,-0.3827))
	table.add('1111', Point(-0.7071,-0.7071))
	table.add('1110', Point(-0.3827,-0.9239))
	table.add('1010', Point(0,-1))
	table.add('1011', Point(0.3827,-0.9239))
	table.add('1001', Point(0.7071,-0.7071))
	table.add('1000', Point(0.9239,-0.3827))
	return table

def modLevels16(bits, encoding):
	modList = []
	table = None
	if encoding == LINEAR:
		table = createMod16LinearLookupTable()
	else:
		table = createMod16GrayLookupTable()

	symbols = BSH.divideIntoBitStrings(bits, 4)
	for symbol in symbols:
		moddedSymbol = table.getSymbol(symbol)
		modList.append(moddedSymbol)
	return modList


def demodLevels2(symbols):
	bits = []
	table = createMod2LookupTable()
	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits


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


def demodLevels8(symbols, encoding):
	bits = []
	table = None
	if encoding == LINEAR:
		table = createMod8LinearLookupTable()
	else:
		table = createMod8GrayLookupTable()

	for symbol in symbols:
		bits.extend(table.getBestMatchingBitSequence(symbol))
	return bits

def demodLevels16(symbols, encoding):
	bits = []
	table = None
	if encoding == LINEAR:
		table = createMod16LinearLookupTable()
	else:
		table = createMod16GrayLookupTable()

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


def demod(symbols, levels, encoding):
	if levels == 2:
		return demodLevels2(symbols)
	if levels == 4:
		return demodLevels4(symbols, encoding)
	if levels == 8:
		return demodLevels8(symbols, encoding)
	if levels == 16:
		return demodLevels16(symbols, encoding)