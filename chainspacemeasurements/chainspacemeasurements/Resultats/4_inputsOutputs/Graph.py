# Read results files and create a error graph
import numpy as np
import matplotlib.pyplot as plt
import ast

minSh = 2
maxSh = 5   # put +1 than you need


#fullcross
filename = "clever_SH"
tpsMean = []
tpsStd  = []
LatMean = []
LatStd  = []

for i in range(minSh, maxSh):
	file = filename+str(i)+"_mode7.txt"
	f = open(file, "r")
	count = 0
	for line in f:
		if count < 4:
			line = line.split(" ")
			x = ast.literal_eval(line[1])


			if count == 0:   tpsMean.append(x[0]*i) 
			elif count == 1: tpsStd.append(float(line[1]))
			elif count == 2: LatMean.append(x[0])
			elif count == 3: LatStd.append(float(line[1]))
			count += 1

### nocross ###
filename2 = "random_SH"
tpsMeanRand = []
tpsStdRand  = []
LatMeanRand = []
LatStdRand  = []

for i in range(minSh, maxSh):
	file = filename2+str(i)+"_mode7.txt"
	f = open(file, "r")
	count = 0
	for line in f:
		if count < 4:
			line = line.split(" ")
			x = ast.literal_eval(line[1])

			if count == 0:   tpsMeanRand.append(x[0]*i) 
			elif count == 1: tpsStdRand.append(float(line[1]))
			elif count == 2: LatMeanRand.append(x[0])
			elif count == 3: LatStdRand.append(float(line[1]))
			count += 1




#### fullcross ####

asymetricerrorStd = [tpsStd, tpsStd]

x = list(range(minSh, maxSh))
y = tpsMean

fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
ax0.errorbar(x, y, yerr=asymetricerrorStd, fmt='-o', label = "Clever")
ax0.set_ylabel("Tps [s]")
ax0.set_title("Graph done with 4inputs/4outputs (mode 7)")
ax0.grid(True, which = "both")


y = LatMean
asymetricerrorLatency = [LatStd, LatStd]
ax1.errorbar(x, y, yerr=asymetricerrorLatency, fmt='-o', label = "Clever" )
ax1.set_ylabel("Latency[ms]")
ax1.set_xlabel("Number of shard")
ax1.grid(True, which = "both")

#### nocross ####

asymetricerrorStdRand = [tpsStdRand, tpsStdRand]
x = [elem+0.01 for elem in x]
y = tpsMeanRand

ax0.errorbar(x, y, yerr=asymetricerrorStdRand, fmt='-x', label = "Random")

y = LatMeanRand
asymetricerrorLatencyRand = [LatStdRand, LatStdRand]
ax1.errorbar(x, y, yerr=asymetricerrorLatencyRand, fmt='-x', label = "Random")

ax0.legend()
ax1.legend()

plt.savefig("Graph_mode7.png")

plt.show()


