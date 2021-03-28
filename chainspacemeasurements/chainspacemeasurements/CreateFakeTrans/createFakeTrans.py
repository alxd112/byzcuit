##############################
# This file create a a file full of transaction
# that only interact within a same shard
#
##############################
import random

# Parameters: FIXME
nbrShards= 3
nbrTrans = 50000
nbrInput = 2
nbrOuput = 2

f = open("./noFullCross/nofullCross_SH"+str(nbrShards)+"_n_"+str(nbrInput)+".txt", "w")


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

f = open("./fullCross/fullCross_SH"+str(nbrShards)+"_n_"+str(nbrInput)+".txt", "w")


for i in range(nbrTrans):
	allShard = list(range(nbrShards))
	alreadyChosenshard = []
	shard = random.choice([elem for elem in allShard if elem not in alreadyChosenshard])
	#shard = random.randint(0,nbrShards - 1)
	text = ""
	for count in range(nbrInput):
		alreadyChosenshard.append(shard)
		
		text = text + str(shard)
		#print(alreadyChosenshard)

		if len(alreadyChosenshard) == nbrShards:
			alreadyChosenshard = []

		shard = random.choice([elem for elem in allShard if elem not in alreadyChosenshard])

		if count != nbrInput - 1:
			text = text + ","
	
	#print(text)
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
