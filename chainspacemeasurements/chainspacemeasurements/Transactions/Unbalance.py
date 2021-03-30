

nbrTrans = 40000

file = open("unbalance.txt", "w")

counter = 0
for i in range(nbrTrans):
	if counter < 400:
		file.write("0:0\n")
	elif counter < 800:
		file.write("1:1\n")
	else:
		counter = 0
		file.write("0:0\n")
	counter+=1

file.close()

