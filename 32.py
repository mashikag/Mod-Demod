import Encoder
import BitGenerator as BG
import BitStringHelper as BSH

index = 0
values = BG.generateBitList(5)
for i in values:
	print index, BSH.charListToString(Encoder.convertToGray(i))
	index += 1