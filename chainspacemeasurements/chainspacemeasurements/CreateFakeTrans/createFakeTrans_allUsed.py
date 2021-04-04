##############################
# This file create a a file full of transaction
# that only interact within a same shard
#
##############################
import random

# Parameters: FIXME
nbrShards= 4
nbrTrans = 50000
nbrInput = nbrShards
nbrOuput = nbrShards



f = open("./fullCross_inp/fullCrossInp_SH"+str(nbrShards)+"_n_"+str(nbrInput)+".txt", "w")


for i in range(nbrTrans):

	allShard = list(range(nbrShards))
	outshard = random.randint(0,nbrShards - 1)
	text = ""
	for count in range(nbrInput):
		
		text = text + str(count)
		
		if count != nbrInput - 1:
			text = text + ","
	
	#print(text)
	text = text + ":"
	for count in range(nbrOuput):
		text = text + str(outshard)
		if count != nbrOuput - 1:
			text = text + ","
	text = text + "\n"	
	f.write(text)



f.close()
