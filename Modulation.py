import PSK
import QAM

# Test submodule push. Hi Paul!

LINEAR = 0
GRAY = 1

MOD_SCHEME_PSK = 2
MOD_SCHEME_QAM = 3


def mod(input, modScheme, levels, encoding):
	if modScheme == MOD_SCHEME_PSK:
		return PSK.mod(input, levels, encoding)
	if modScheme == MOD_SCHEME_QAM:
		return QAM.mod(input, levels, encoding)


def demod(input, modScheme, levels, encoding):
	if modScheme == MOD_SCHEME_PSK:
		return PSK.demod(input, levels, encoding)
	if modScheme == MOD_SCHEME_QAM:
		return QAM.demod(input, levels, encoding)
