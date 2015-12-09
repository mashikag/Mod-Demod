from point import Point	
import BitStringHelper as BSH

LINEAR = 0
GRAY = 1


def mod2Lookup(bit):
	if bit == '0':
		return Point(-1,0)
	elif bit == '1':
		return Point(1,0)

def modLevels2(bits):
	modList = []
	for bit in bits:
		modList.append(mod2Lookup(bit))
	return modList



def mod4LookupLinear(symbol):
	if symbol == "00":
		return Point(-1,0)
	elif symbol == "01":
		return Point(0, 1)
	elif symbol == "10":
		return Point(1,0)
	else: 						# 1,1
		return Point (0,-1)

def mod4LookupGray(symbol):
	if symbol == "00":
		return Point(1,0)
	elif symbol == "01":
		return Point(0,1)
	elif symbol == "11":
		return Point(-1,0)
	else:						# 1,0
		return Point(0,-1)

def modLevels4(bits, encoding):
	modList = []
	lookupFunction = mod4LookupLinear
	if encoding == GRAY:
		lookupFunction = mod4LookupGray

	symbols = BSH.divideIntoBitStrings(bits, 2)
	for symbol in symbols:
		moddedSymbol = lookupFunction(symbol)
		modList.append(moddedSymbol)

	return modList	



def mod8LookupLinear(symbol):
	if symbol == '000':
		return Point(1,0)
	elif symbol == '001':
		return Point(0.7071, 0.7071)
	elif symbol == '010':
		return Point(0, 1)
	elif symbol == '011':
		return Point(-0.7071, 0.7071)
	elif symbol == '100':
		return Point(-1, 0)
	elif symbol == '101':
		return Point(-0.7071, -0.7071)
	elif symbol == '110':
		return Point(0, -1)
	else: 			#111
		return Point(0.7071, -0.7071)

def mod8LookupGray(symbol):
	if symbol == "000":
		return Point(1,0)
	elif symbol == "001":
		return Point(0.7071, 0.7071)
	elif symbol == "101":
		return Point(0, 1)
	elif symbol == "100":
		return Point(-0.7071, 0.7071)
	elif symbol == "110":
		return Point(-1, 0)
	elif symbol == "111":
		return Point(-0.7071, -0.7071)
	elif symbol == "011":
		return Point(0,-1)
	else:			#010
		return Point(0.7071, -0.7071)

def modLevels8(bits, encoding):
	modList = []
	lookupFunction = mod8LookupLinear
	if encoding == GRAY:
		lookupFunction = mod8LookupGray

	symbols = BSH.divideIntoBitStrings(bits, 3)
	for symbol in symbols:
		moddedSymbol = lookupFunction(symbol)
		modList.append(moddedSymbol)

	return modList




def modulate(bits, levels, encoding):
	if levels == 2:
		return modLevels2(bits)
	if levels == 4: 
		return modLevels4(bits, encoding)
	if levels == 8:
		return modLevels8(bits, encoding)