# Read results files and create a error graph
import numpy as np
import matplotlib.pyplot as plt
import ast
from collections import Counter

mode = 5
minSh = 2
maxSh = 8   # put +1 than you need
minInput = 2
maxInput = 3# put +1 than you need
shardList = [2, 3, 4, 5, 6, 7, 8, 9, 10]

#Clever
filename = "Clever/clever"
tpsMean = []
tpsStd  = []
LatMean = []
LatStd  = []
allTps  = x = [[] for i in range(10)]
for i in shardList:
	file = filename+str(i)+".txt"
	f = open(file, "r")
	count = 0
	print(i)
	for line in f:
		if count <=5:
			if count <5:
				line = line.split(" ")
			if count != 4:
				x = ast.literal_eval(line[1])


			if count == 0:   tpsMean.append(x[0]*i) 
			elif count == 1: tpsStd.append(float(line[1]))
			elif count == 2: LatMean.append(x[0])
			elif count == 3: LatStd.append(float(line[1]))
			elif count == 4: pass
			elif count == 5: 
				print(ast.literal_eval(line))
				allTps[i-1].append(ast.literal_eval(line))
			count += 1

### Rabdom ###
filename2 = "Random/random"
tpsMeanRand = []
tpsStdRand  = []
LatMeanRand = []
LatStdRand  = []
allTpsRand  = x = [[] for i in range(10)]

for i in shardList:
	file = filename2+str(i)+".txt"
	f = open(file, "r")
	count = 0
	for line in f:
		if count <=5:
			if count <5:
				line = line.split(" ")
			if count != 4:
				x = ast.literal_eval(line[1])


			if count == 0:   tpsMeanRand.append(x[0]*i) 
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
ax0.errorbar(x, y, yerr=asymetricerrorStd, fmt='-o', label = "DAVIS")
ax0.set_ylabel("Tps")
ax0.set_title("Evolution of the tps and latency in function of the nbr of shards")
ax0.grid(True, which = "both")


y = LatMean
asymetricerrorLatency = [LatStd, LatStd]
ax1.errorbar(x, y, yerr=asymetricerrorLatency, fmt='-o', label = "DAVIS" )
ax1.set_ylabel("Latency[ms]")
ax1.set_xlabel("Number of shards")
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




rows = len(shardList)
fig, ax = plt.subplots(rows, 
					   sharex='col',figsize=(10,10))
					   #sharey='row')
ax[0].set_title("Distribution of the tps in function of the number of shard used")

for row in range(rows):
	nbr = len(allTps[shardList[row]-1][0])
	y = [0]*nbr
	ax[row].scatter(allTps[shardList[row]-1][0], y, label = 'DAVIS')
	ax[row].set_ylabel('shard:'+str(shardList[row]))

	
	nbr = len(allTpsRand[shardList[row]-1][0])
	y = [0.5]*nbr	
	ax[row].scatter(allTpsRand[shardList[row]-1][0], y, label = 'random')
	ax[row].legend()
plt.xlabel("Tps")
plt.savefig("Graph_distrib_Clever_Random.png")



###########################
"""
100 blocks
Clever
edges || trans
2 15.01  28.30
3 18.46	 35.41
4 20.47  38.87
5 18.97  41.52
6 21.92  42.94
7 22.51  44.08
8 26.21  44.70
9 24.33  45.67
10 26.86 46.71



random
2 49.818 59.79
3 66.23  66.23
4 75.14  75.14
5 80.37  85.39
6 83.37  88.09
7 84.93  89.74
8 87.93  90.91
9 88.59  92.12
10 90.14 92.94
"""

crossEdge = [15.01, 18.46, 20.47, 18.97, 21.92, 22.51, 26.21, 24.33, 26.86]
crossTran = [28.30, 35.41, 38.87, 41.52, 42.94, 44.08, 44.70, 45.67, 46.71]

rcrossEdge = [49.81, 66.23, 75.14, 80.37, 83.37, 84.93, 87.93, 88.59, 90.14]
rcrossTran = [59.79, 66.23, 75.14, 85.39, 88.09, 89.74, 90.91, 92.12, 92.94]

fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
ax0.plot(shardList, crossTran, label = "DAVIS cross trans")
ax0.plot(shardList, rcrossTran, label = "Random cross trans")

ax0.set_ylabel("Percentage [%]")
ax0.set_title("Evolution of the Percentage of cross transactions\n and cross edges in function of the nbr of shards")
ax0.grid(True, which = "both")


ax1.plot(shardList, crossEdge, label = "DAVIS cross edges" )
ax1.plot(shardList, rcrossEdge, label = "Random cross edges" )

ax1.set_ylabel("Percentage [%]")
ax1.set_xlabel("Number of shards")
ax1.grid(True, which = "both")

ax0.legend()
ax1.legend()

plt.savefig("Graph_Clever_Random_percentage.png")
