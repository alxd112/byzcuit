# Read results files and create a error graph
import numpy as np
import matplotlib.pyplot as plt
import ast
from collections import Counter

minSh = 2
maxSh = 5   # put +1 than you need
minInput = 1
maxInput = 5# put +1 than you need
shardList = [2,3,4,8,9,10]

#Clever
filename = "Clever_SH"
tpsMean = []
tpsStd  = []
LatMean = []
LatStd  = []
allTps  = x = [[] for i in range(10)]
for i in shardList:
	file = filename+str(i)+"_n1_range1.txt"
	f = open(file, "r")
	count = 0
	print(i)
	for line in f:
		if count <=5:
			if count <5:
				line = line.split(" ")
			if count != 4:
				x = ast.literal_eval(line[1])


			if count == 0:   tpsMean.append(x[0]) 
			elif count == 1: tpsStd.append(float(line[1]))
			elif count == 2: LatMean.append(x[0])
			elif count == 3: LatStd.append(float(line[1]))
			elif count == 4: pass
			elif count == 5: 
				print(ast.literal_eval(line))
				allTps[i-1].append(ast.literal_eval(line))
			count += 1

### Rabdom ###
filename2 = "Random_SH"
tpsMeanRand = []
tpsStdRand  = []
LatMeanRand = []
LatStdRand  = []
allTpsRand  = x = [[] for i in range(10)]

for i in shardList:
	file = filename2+str(i)+"_n1_range1.txt"
	f = open(file, "r")
	count = 0
	for line in f:
		if count <=5:
			if count <5:
				line = line.split(" ")
			if count != 4:
				x = ast.literal_eval(line[1])


			if count == 0:   tpsMeanRand.append(x[0]) 
			elif count == 1: tpsStdRand.append(float(line[1]))
			elif count == 2: LatMeanRand.append(x[0])
			elif count == 3: LatStdRand.append(float(line[1]))
			elif count == 4: pass
			elif count == 5: 
				#print(x)
				allTpsRand[i-1].append(ast.literal_eval(line))
			count += 1




#### fullcross ####

asymetricerrorStd = [tpsStd, tpsStd]

x = shardList
y = tpsMean
fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
ax0.errorbar(x, y, yerr=asymetricerrorStd, fmt='-o', label = "Clever")
ax0.set_ylabel("Tps [s]")
ax0.set_title("Graph done with 4 shards")
ax0.grid(True, which = "both")


y = LatMean
asymetricerrorLatency = [LatStd, LatStd]
ax1.errorbar(x, y, yerr=asymetricerrorLatency, fmt='-o', label = "Clever" )
ax1.set_ylabel("Latency[ms]")
ax1.set_xlabel("Number of input and ouput/transaction")
ax1.grid(True, which = "both")

#### nocross ####

asymetricerrorStdRand = [tpsStdRand, tpsStdRand]
x = [elem+0.05 for elem in x]
y = tpsMeanRand

ax0.errorbar(x, y, yerr=asymetricerrorStdRand, fmt='-x', label = "Random")

y = LatMeanRand
asymetricerrorLatencyRand = [LatStdRand, LatStdRand]
ax1.errorbar(x, y, yerr=asymetricerrorLatencyRand, fmt='-x', label = "Random")

ax0.legend()
ax1.legend()

plt.savefig("Graph_Clever_Random.png")

# plt.show()




rows = 6
fig, ax = plt.subplots(rows, 
					   sharex='col',figsize=(10,10))
					   #sharey='row')
ax[0].set_title("Distribution of the tps in function of the number of shard used (50k transactions used)")

for row in range(rows):
	nbr = len(allTps[shardList[row]-1][0])
	y = [0]*nbr
	ax[row].scatter(allTps[shardList[row]-1][0], y, label = 'clever')
	ax[row].set_ylabel('shard:'+str(shardList[row]))

	
	nbr = len(allTpsRand[shardList[row]-1][0])
	y = [0.5]*nbr	
	ax[row].scatter(allTpsRand[shardList[row]-1][0], y, label = 'random')
	ax[row].legend()
plt.xlabel("Tps [s]")
plt.savefig("Graph_distrib_Clever_Random.png")

