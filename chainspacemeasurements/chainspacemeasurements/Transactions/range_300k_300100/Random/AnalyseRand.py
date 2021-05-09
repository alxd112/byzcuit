# Read results files and create a error graph
import numpy as np
import matplotlib.pyplot as plt
import ast



#fullcross
filename = "Random_3Mode_6.txt"
nbrshards = 3


f = open(filename, "r")
count = 0
x = [0]
one = [0]
zero = [0]
deux = [0]
un = 0
zer = 0
deu = 0
for line in f:
	un = one[count]
	zer = zero[count]
	deu = deux[count]
	li = line.split(":")
	inp = li[0].split(",")
	out = li[1].split(",")
	# for elem in inp:
	# 	if elem == '1':
	# 		un +=1
	# 	else:
	# 		zer +=1
	#for elem in out:
	elem = out[0].rstrip("\n")
	elem = str(elem)
	if elem == '2':
		deu += 1
	elif elem == '1':
		un +=1
	elif elem == '0':
		zer += 1
	else:
		print("problem")
		e = 0
	one.append(un)
	zero.append(zer)
	deux.append(deu)
	x.append(count)
	count += 1
	

plt.plot(x, one, label = "one")
plt.plot(x, zero, label = "zero")
plt.plot(x, deux, label = "deux")
plt.title("Graph of the cumulative number of transactions\n per shard for each arriving transaction with "+str(nbrshards)+"shards")
plt.xlabel("Nbr of arrived transactions")
plt.ylabel("Nbr of transactions placed in shard X")
plt.legend()
plt.savefig("load.png")