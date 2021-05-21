# Read results files and create a error graph
import numpy as np
import matplotlib.pyplot as plt
import ast



for i in [2,3,4,5,6,7,8,9,10]:
	#fullcross
	filename = "Clever_3Mode_5relax.txt"
	filename = "Clever_"+str(i)+"Mode_5relax.txt"

	nbrshards = i
	print(i)
	f = open(filename, "r")
	count = 0
	tab = [[0] for elem in range(nbrshards)]

	x = [0]
	# one = [0]
	# zero = [0]
	# deux = [0]
	# un = 0
	# zer = 0
	# deu = 0
	print(tab)
	for line in f:
		# un = one[count]
		# zer = zero[count]
		# deu = deux[count]
		li = line.split(":")
		inp = li[0].split(",")
		out = li[1].split(",")
		# for elem in inp:
		# 	if elem == '1':
		# 		un +=1
		# 	else:
		# 		zer +=1
		elem = out[0].rstrip("\n")
		elem = int(elem)
		for i in range(nbrshards):
			if i == elem:
				tab[i].append(tab[i][-1] + 1)
			else:
				tab[i].append(tab[i][-1])
		# if elem == '2':
		# 	deu += 1
		# elif elem == '1':
		# 	un +=1
		# elif elem == '0':
		# 	zer += 1
		# else:
		# 	print("problem")
		# 	e = 0
		# one.append(un)
		# zero.append(zer)
		# deux.append(deu)
		x.append(count)
		count += 1
	print(len(x))
	plt.figure(nbrshards)	
	for j in range(nbrshards):
		print(len(tab[j]))
		plt.plot(x, tab[j], label = str(j))
	plt.title("Graph of the cumulative number of transactions\n per shard for each arriving transaction with "+str(nbrshards)+"shards")
	plt.xlabel("Nbr of arrived transactions")
	plt.ylabel("Nbr of transactions placed in shard X")
	plt.legend()
	plt.savefig("load"+str(nbrshards)+"relax.png")