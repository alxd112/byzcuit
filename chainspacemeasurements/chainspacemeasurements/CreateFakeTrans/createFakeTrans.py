##############################
# This file create a a file full of transaction
# that only interact within a same shard
#
##############################
import random

# Parameters: FIXME
nbrShards= 2
nbrTrans = 50000
nbrInput = 1
nbrOuput = 1

f = open("NoCrossTrans_SH"+str(nbrShards)+".txt", "w")


for i in range(nbrTrans):
	shard = random.randint(0,nbrShards - 1)
	text = ""
	for count in range(nbrInput):
		text = text + str(shard)
		if count != nbrInput - 1:
			text = text + ","
	text = text + ":"
	for count in range(nbrOuput):
		text = text + str(shard)
		if count != nbrOuput - 1:
			text = text + ","
	text = text + "\n"	
	f.write(text)



f.close()

f = open("fullCross_SH"+str(nbrShards)+".txt", "w")


for i in range(nbrTrans):
	shard = random.randint(0,nbrShards - 1)
	text = ""
	for count in range(nbrInput):
		text = text + str(shard)
		if count != nbrInput - 1:
			text = text + ","
	text = text + ":"
	outShard = -1
	while (outShard == -1 or (outShard != -1 and outShard == shard)):
		outShard = random.randint(0,nbrShards - 1)

	for count in range(nbrOuput):
		text = text + str(outShard)
		if count != nbrOuput - 1:
			text = text + ","
	text = text + "\n"	
	f.write(text)



f.close()
