# Read results files and create a error graph
import numpy as np
import matplotlib.pyplot as plt
import ast

minSh = 2
maxSh = 5   # put +1 than you need
minInput = 1
maxInput = 5# put +1 than you need

#fullcross
filename = "nbrOfInputs_medium/fullcross_SH4_n"
tpsMean = []
tpsStd  = []
LatMean = []
LatStd  = []

for i in range(minInput, maxInput):
	file = filename+str(i)+"_med.txt"
	f = open(file, "r")
	count = 0
	for line in f:
		line = line.split(" ")
		x = ast.literal_eval(line[1])


		if count == 0:   tpsMean.append(x[0]*4) 
		elif count == 1: tpsStd.append(float(line[1]))
		elif count == 2: LatMean.append(x[0])
		elif count == 3: LatStd.append(float(line[1]))
		count += 1

### nocross ###
filename2 = "nbrOfInputs_medium/nofullcross_SH4_n"
tpsMeanRand = []
tpsStdRand  = []
LatMeanRand = []
LatStdRand  = []

for i in range(minInput, maxInput):
	file = filename2+str(i)+"_med.txt"
	f = open(file, "r")
	count = 0
	for line in f:
		line = line.split(" ")
		x = ast.literal_eval(line[1])

		if count == 0:   tpsMeanRand.append(x[0]*4) 
		elif count == 1: tpsStdRand.append(float(line[1]))
		elif count == 2: LatMeanRand.append(x[0])
		elif count == 3: LatStdRand.append(float(line[1]))
		count += 1




#### fullcross ####

asymetricerrorStd = [tpsStd, tpsStd]

x = list(range(minInput, maxInput))
y = tpsMean

fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
ax0.errorbar(x, y, yerr=asymetricerrorStd, fmt='-o', label = "fullcross")
ax0.set_ylabel("Tps [s]")
ax0.set_title("Graph done with 4 shards")
ax0.grid(True, which = "both")


y = LatMean
asymetricerrorLatency = [LatStd, LatStd]
ax1.errorbar(x, y, yerr=asymetricerrorLatency, fmt='-o', label = "fullcross" )
ax1.set_ylabel("Latency[ms]")
ax1.set_xlabel("Number of input and ouput/transaction")
ax1.grid(True, which = "both")

#### nocross ####

asymetricerrorStdRand = [tpsStdRand, tpsStdRand]
x = [elem+0.01 for elem in x]
y = tpsMeanRand

ax0.errorbar(x, y, yerr=asymetricerrorStdRand, fmt='-x', label = "nocross")

y = LatMeanRand
asymetricerrorLatencyRand = [LatStdRand, LatStdRand]
ax1.errorbar(x, y, yerr=asymetricerrorLatencyRand, fmt='-x', label = "nocross")

ax0.legend()
ax1.legend()

plt.savefig("Graph_var_nbrInput.png")

#plt.show()



###############################################################
###############################################################


#fullcross
filename = "nbrOfShard_medium/fullcross_SH"
tpsMean = []
tpsStd  = []
LatMean = []
LatStd  = []

for i in range(minSh, maxSh):
	file = filename+str(i)+"_n2_med.txt"
	f = open(file, "r")
	count = 0
	for line in f:
		line = line.split(" ")
		x = ast.literal_eval(line[1])


		if count == 0:   tpsMean.append(x[0]*i) 
		elif count == 1: tpsStd.append(float(line[1]))
		elif count == 2: LatMean.append(x[0])
		elif count == 3: LatStd.append(float(line[1]))
		count += 1

### nocross ###
filename2 = "nbrOfShard_medium/nofullcross_SH"
tpsMeanRand = []
tpsStdRand  = []
LatMeanRand = []
LatStdRand  = []

for i in range(minSh, maxSh):
	file = filename2+str(i)+"_n2_med.txt"
	f = open(file, "r")
	count = 0
	for line in f:
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
print(x)
print(y)
fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
ax0.errorbar(x, y, yerr=asymetricerrorStd, fmt='-o', label = "fullcross")
ax0.set_ylabel("Tps [s]")
ax0.set_title("Graph done with 2 inputs and 2 outputs")
ax0.grid(True, which = "both")


y = LatMean
asymetricerrorLatency = [LatStd, LatStd]
ax1.errorbar(x, y, yerr=asymetricerrorLatency, fmt='-o', label = "fullcross" )
ax1.set_ylabel("Latency[ms]")
ax1.set_xlabel("Number of shard")
ax1.grid(True, which = "both")

#### nocross ####

asymetricerrorStdRand = [tpsStdRand, tpsStdRand]
x = [elem+0.01 for elem in x]
y = tpsMeanRand
print(y)
ax0.errorbar(x, y, yerr=asymetricerrorStdRand, fmt='-x', label = "nocross")

y = LatMeanRand
asymetricerrorLatencyRand = [LatStdRand, LatStdRand]
ax1.errorbar(x, y, yerr=asymetricerrorLatencyRand, fmt='-x', label = "nocross")

ax0.legend()
ax1.legend()

plt.savefig("Graph_var_nbrShard.png")

#plt.show()




###############################################################
###############################################################


#fullcross
filename = "nbr_inpAndshard/fullCrossInp_SH"
tpsMean = []
tpsStd  = []
LatMean = []
LatStd  = []

for i in range(minSh, maxSh):
	file = filename+str(i)+"_n"+str(i)+"_range1.txt"
	f = open(file, "r")
	count = 0
	for line in f:
		if count <=3:

			line = line.split(" ")
			x = ast.literal_eval(line[1])


			if count == 0:   tpsMean.append(x[0]*i) 
			elif count == 1: tpsStd.append(float(line[1]))
			elif count == 2: LatMean.append(x[0])
			elif count == 3: LatStd.append(float(line[1]))
		count += 1

### nocross ###
filename2 = "nbr_inpAndshard/nofullcrossInp_SH"
tpsMeanRand = []
tpsStdRand  = []
LatMeanRand = []
LatStdRand  = []

for i in range(minSh, maxSh):
	file = filename2+str(i)+"_n"+str(i)+".txt"
	f = open(file, "r")
	count = 0
	for line in f:
		if count <=3:
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
print(x)
print(y)
fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
ax0.errorbar(x, y, yerr=asymetricerrorStd, fmt='-o', label = "fullcrossInp")
ax0.set_ylabel("Tps [s]")
ax0.set_title("Graph done with 50000 transactions")
ax0.grid(True, which = "both")


y = LatMean
asymetricerrorLatency = [LatStd, LatStd]
ax1.errorbar(x, y, yerr=asymetricerrorLatency, fmt='-o', label = "fullcrossInp" )
ax1.set_ylabel("Latency[ms]")
ax1.set_xlabel("Number of shard/inputs/outputs")
ax1.grid(True, which = "both")

#### nocross ####

asymetricerrorStdRand = [tpsStdRand, tpsStdRand]
x = [elem+0.01 for elem in x]
y = tpsMeanRand
print(y)
ax0.errorbar(x, y, yerr=asymetricerrorStdRand, fmt='-x', label = "nocross")

y = LatMeanRand
asymetricerrorLatencyRand = [LatStdRand, LatStdRand]
ax1.errorbar(x, y, yerr=asymetricerrorLatencyRand, fmt='-x', label = "nocross")

ax0.legend()
ax1.legend()

plt.savefig("Graph_var_nbrShard_input.png")

#plt.show()