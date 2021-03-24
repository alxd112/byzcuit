# Read results files and create a error graph
import numpy as np
import matplotlib.pyplot as plt
import ast

minSh = 2
maxSh = 5

#Clever
filename = "Resultats/True/Clever_"
tpsMean = []
tpsStd  = []
LatMean = []
LatStd  = []

for i in range(minSh, maxSh):
	file = filename+str(i)+".txt"
	f = open(file, "r")
	count = 0
	for line in f:
		line = line.split(" ")
		print(line)
		x = ast.literal_eval(line[1])

		if count == 0:   tpsMean.append(x[0]*i) 
		elif count == 1: tpsStd.append(float(line[1]))
		elif count == 2: LatMean.append(x[0])
		elif count == 3: LatStd.append(float(line[1]))
		count += 1

### Random ###
filename2 = "Resultats/True/Random_"
tpsMeanRand = []
tpsStdRand  = []
LatMeanRand = []
LatStdRand  = []

for i in range(minSh, maxSh):
	file = filename2+str(i)+".txt"
	f = open(file, "r")
	count = 0
	for line in f:
		line = line.split(" ")
		print(line)
		x = ast.literal_eval(line[1])

		if count == 0:   tpsMeanRand.append(x[0]*i) 
		elif count == 1: tpsStdRand.append(float(line[1]))
		elif count == 2: LatMeanRand.append(x[0])
		elif count == 3: LatStdRand.append(float(line[1]))
		count += 1




#### Clever ####

asymetricerrorStd = [tpsStd, tpsStd]

x = list(range(minSh, maxSh))
y = tpsMean
print(x)
print(y)
fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
ax0.errorbar(x, y, yerr=asymetricerrorStd, fmt='-o', label = "clever")
ax0.set_ylabel("Tps [s]")
ax0.grid(True, which = "both")


y = LatMean
asymetricerrorLatency = [LatStd, LatStd]
ax1.errorbar(x, y, yerr=asymetricerrorLatency, fmt='-o', label = "clever" )
ax1.set_ylabel("Latency[ms]")
ax1.grid(True, which = "both")

#### Random ####

asymetricerrorStdRand = [tpsStdRand, tpsStdRand]
x = [elem+0.005 for elem in x]
y = tpsMeanRand
print(y)
ax0.errorbar(x, y, yerr=asymetricerrorStdRand, fmt='-x', label = "random")

y = LatMeanRand
asymetricerrorLatencyRand = [LatStdRand, LatStdRand]
ax1.errorbar(x, y, yerr=asymetricerrorLatencyRand, fmt='-x', label = "random")

ax0.legend()
ax1.legend()

plt.savefig("measures.png")

plt.show()