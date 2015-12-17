import PSK
import QAM
import math

# Test submodule push. Hi Paul!

LINEAR = 0
GRAY = 1

MOD_SCHEME_PSK = 2
MOD_SCHEME_QAM = 3


def mod(input, modScheme, levels, encoding):
	bitsPerSymbol = int(math.log(levels,2))
	
	# Fails if it is not possible to modulate the number of bits passed
	# given the number of bits per symbol
	assert (len(input) % bitsPerSymbol == 0)

	if modScheme == MOD_SCHEME_PSK:
		return PSK.mod(input, levels, encoding)
	if modScheme == MOD_SCHEME_QAM:
		return QAM.mod(input, levels, encoding)


def demod(input, modScheme, levels, encoding):
	if modScheme == MOD_SCHEME_PSK:
		return PSK.demod(input, levels, encoding)
	if modScheme == MOD_SCHEME_QAM:
		return QAM.demod(input, levels, encoding)
