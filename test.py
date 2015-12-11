import QAM
import BitStringHelper as BSH
import BitGenerator as BG


def test(numberOfBits, numberOfLevels, encoding):
	failures = 0
	values = BG.generateBitList(numberOfBits)

	encString = "Linear"
	if encoding == 1:
		encString = "Gray"

	print "\n{} QAM {} - number of permutations to test: {}".format(numberOfLevels, encString,len(values))
	for value in values: 
		mod = QAM.mod(value, numberOfLevels, encoding)
		demod = QAM.demod(mod, numberOfLevels, encoding)
		print value, " = ", demod
		if value != demod:
			failures += 1
	print "{} QAM {} failures: {}\n".format(numberOfLevels,encString,failures)



# Testing 2-QAM
test(1,2,0)


# Testing 4-QAM Linear
test(2,4,0)


# Testing 4-QAM Gray
test(2,4,1)




# 8 QAM Linear
test(3,8,0)



# 8 QAM Gary
test(3,8,1)


# 16 QAM Linear
test(4,16,0)


# 16 QAM Gray
test(4,16,1)




# 64 QAM Linear
test(6,64,0)


# 64 QAM Gray
test(6,64,1)




# 256 QAM Linear
test(8,256,0)


# 256 QAM Gray
test(8,256,1)





# 1024 QAM Linear
test(10,1024,0)


# 1024 QAM Gray
test(10,1024,1)



# 32 QAM Linear
test(5,32,0)


# 32 QAM Gray
test(5,32,1)




# 128 QAM Linear
test(7,128,0)


# 128 QAM Gray
test(7,128,1)





# 512 QAM Linear
test(9,512,0)


# 128 QAM Gray
test(9,512,1)