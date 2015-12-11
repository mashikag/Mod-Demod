import QAM
import BitStringHelper as BSH


# 2-QAM
test = "11001001"
input = BSH.stringToCharList(test)
mod = QAM.mod(input, 2, 0)
demod = QAM.demod(mod, 2, 0)

if (input == demod):
	print "2-QAM pass"
else:
	print "2-QAM fail"


# 4 QAM Linear
mod = QAM.mod(input, 4, 0)
demod = QAM.demod(mod, 4, 0)

if(input == demod):
	print "4-QAM Linear pass"
else:
	print "4-QAM Linear fail"


# 4 QAM Gray
mod = QAM.mod(input, 4, 1)
demod = QAM.demod(mod, 4, 1)

if(input == demod):
	print "4-QAM Gray pass"
else:
	print "4-QAM Gray fail"


# 8 QAM Linear
test = "111000101"
input = BSH.stringToCharList(test)
mod = QAM.mod(input, 8, 0)
demod = QAM.demod(mod, 8, 0)

if(input == demod):
	print "8-QAM Linear pass"
else:
	print "8-QAM Linear fail"


# 8 QAM Gray
mod = QAM.mod(input, 8, 1)
demod = QAM.demod(mod, 8, 1)

if(input == demod):
	print "8-QAM Gray pass"
else:
	print "8-QAM Gray fail"



# 16 QAM Linear
test = "1111000011000011"
input = BSH.stringToCharList(test)
mod = QAM.mod(input, 16, 0)
demod = QAM.demod(mod, 16, 0)

if(input == demod):
	print "16-QAM Linear pass"
else:
	print "16-QAM Linear fail"


# 16 QAM Gray
mod = QAM.mod(input, 16, 1)
demod = QAM.demod(mod, 16, 1)

if(input == demod):
	print "16-QAM Gray pass"
else:
	print "16-QAM Gray fail"




# 64 QAM Linear
test = "111111000000111000000111"
input = BSH.stringToCharList(test)
mod = QAM.mod(input, 64, 0)
demod = QAM.demod(mod, 64, 0)

if(input == demod):
	print "64-QAM Linear pass"
else:
	print "64-QAM Linear fail"


# 64 QAM Gray
mod = QAM.mod(input, 64, 1)
demod = QAM.demod(mod, 64, 1)

if(input == demod):
	print "64-QAM Gray pass"
else:
	print "64-QAM Gray fail"





# 256 QAM Linear
test = "00000000111111110000111111110000"
input = BSH.stringToCharList(test)
mod = QAM.mod(input, 256, 0)

demod = QAM.demod(mod,256, 0)

if(input == demod):
	print "256-QAM Linear pass"
else:
	print "256-QAM Linear fail"


# 256 QAM Gray
mod = QAM.mod(input, 256, 1)
demod = QAM.demod(mod,256, 1)

if(input == demod):
	print "256-QAM Gray pass"
else:
	print "256-QAM Gray fail"





# 1024 QAM Linear
test = "0000000000111111111100000111111111100000"
input = BSH.stringToCharList(test)
mod = QAM.mod(input, 1024, 0)

demod = QAM.demod(mod,1024, 0)

if(input == demod):
	print "1024-QAM Linear pass"
else:
	print "1024-QAM Linear fail"


# 1024 QAM Gray
mod = QAM.mod(input, 1024, 1)
demod = QAM.demod(mod,1024, 1)

if(input == demod):
	print "1024-QAM Gray pass"
else:
	print "1024-QAM Gray fail"



# 32 QAM Linear
test = "00000111110011111000"
input = BSH.stringToCharList(test)
mod = QAM.mod(input, 32, 0)

demod = QAM.demod(mod, 32, 0)

if(input == demod):
	print "32-QAM Linear pass"
else:
	print "32-QAM Linear fail"


# 32 QAM Gray
mod = QAM.mod(input, 32, 1)
demod = QAM.demod(mod,32, 1)

if(input == demod):
	print "32-QAM Gray pass"
else:
	print "32-QAM Gray fail"




# 128 QAM Linear
test = "0000000111111100011111110000"
input = BSH.stringToCharList(test)
mod = QAM.mod(input, 128, 0)

demod = QAM.demod(mod, 128, 0)

if(input == demod):
	print "128-QAM Linear pass"
else:
	print "128-QAM Linear fail"


# 128 QAM Gray
mod = QAM.mod(input, 128, 1)
demod = QAM.demod(mod,128, 1)

if(input == demod):
	print "128-QAM Gray pass"
else:
	print "128-QAM Gray fail"