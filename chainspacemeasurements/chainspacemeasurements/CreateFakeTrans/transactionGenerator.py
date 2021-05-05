#!python
# THIS CODE IS USED TO CREATE TEXT FILES FOR CHAINSPACE

#############
# IMPORTS
#############

import random
import reader

#############
# Create a text file for ChainSpace with a given percentage of cross
#############


User = "Max" 				# Set to anything except "Max" when Alexandre is running the program, "Max" is when Maxime is running it
if(User == "Max"):
	path = "/media/maxime/My Passport/MasterThesis/blocks"
	path2 = '/home/maxime/Documents/Mémoire'

else:
	path = "/media/alexandre/AlexLinux/blockchain/blocks"
	path2 = '/home/alexandre/Desktop/thesis'

percentageCross = 0.6 	# desired proportion of cross shard transactions (= cross shard edges in this case)
nbrTrans = 100000	# total number of transactions desired
nbrShards = 3			# number of shards in the network

fileToWrite = open(path2 + "/UTXO_Graph_Analysis/Implem/ChainSpaceMeasures/ArtificialTrans/Trans" + str(nbrTrans) + "Cross" + str(percentageCross) + ".txt", "w+")
text = ""

for trans in range(nbrTrans):
	randomizer = random.random()

	if randomizer > percentageCross: # no cross transaction
		inp = random.randint(0, nbrShards - 1)
		out = inp
		text += str(inp) + ":" + str(out) + "\n"

	else: # cross transaction
		inp = random.randint(0, nbrShards - 1)
		out = (inp + 1) % nbrShards
		text += str(inp) + ":" + str(out) + "\n"

fileToWrite.write(text)

#############
# Read the created text file for ChainSpace with a given percentage of cross
#############
nedges, ncrosedges, ntrans, ncrostrans = reader.main(fileToWrite, False, path2, "NoFolder")
print("Created for ChainSpace : " + str(ncrosedges) + "/" + str(nedges) + " cross edges and " + str(ncrostrans) + "/" + str(ntrans) + " cross transactions" )
print(" Asked : " + str(percentageCross) + " obtained -> " + str(100.0 * float(ncrosedges)/float(nedges)) + "% of cross edges")
print(" Asked : " + str(percentageCross) + " obtained -> " + str(100.0 * float(ncrostrans)/float(ntrans)) + "% of cross transactions")
