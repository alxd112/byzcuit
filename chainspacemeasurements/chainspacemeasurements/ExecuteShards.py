import os
import time
import serial

minSH = 10
maxSH = 10
nbrRuns = 10
nbrTrans = 46697
Tests = ["Clever"]#"Random", 

for i in range(minSH, maxSH + 1):

	print("|||||||||||||||||||")
	print("||||| "+str(i)+" |||||")
	print("|||||||||||||||||||")

	nbrValidators = i*3
	nbrClients = i * 8

	os.system('python -c \'from chainspacemeasurements.instances import ChainspaceNetwork; n = ChainspaceNetwork(0); n.launch('+str(nbrValidators)+',0); n.launch('+str(nbrClients)+',1);\'')
	print("wait 50 sec then install")
	wait = 60*(i/2.0)
	time.sleep(120)
	os.system('python -c \'from chainspacemeasurements.instances import ChainspaceNetwork; n = ChainspaceNetwork(0); n.ssh_connect(0); n.ssh_connect(1); n.install_deps(0); n.install_deps(1); n.install_core(0); n.install_core(1);\'')
	
	#os.system('/home/alexandre/Desktop/test_aws/try3withenvi/byzcuit/chainspacemeasurements/chainspacemeasurements/pydat.sh')
	#os.system("/pydat.sh")
	time.sleep(5)

	# sudoPassword = '%'
	# command = 'mount -t vboxsf myfolder /home/myuser/myfolder'
	# os.system('echo %s|sudo -S %s' % (sudoPassword, command))

	print("wait 10 sec then run")
	time.sleep(5)
	for version in Tests:

		if version == "Random":
			directory = "Random"
		else:
			directory = "CleverNT"
		print('    python tester.py sharding_measurements 3 3 '+str(nbrTrans)+' '+str(i)+' '+str(nbrRuns)+' /'+str(directory)+'/'+str(version)+'_'+str(i)+'Mode_4.txt '+str(version)+'_SH'+str(i)+'_n1_range1.txt Bullhit.txt')
		os.system('python tester.py sharding_measurements 3 3 '+str(nbrTrans)+' '+str(i)+' '+str(nbrRuns)+' /'+str(directory)+'/'+str(version)+'_'+str(i)+'Mode_4.txt '+str(version)+'_SH'+str(i)+'_n1_range1.txt Bullhit.txt')
		# sudoPassword = '%'
		# command = 'mount -t vboxsf myfolder /home/myuser/myfolder'
		# os.system('echo %s|sudo -S %s' % (sudoPassword, command))
		time.sleep(5)


		time.sleep(2)
	os.system('python -c \'from chainspacemeasurements.instances import ChainspaceNetwork; n = ChainspaceNetwork(0); n.terminate(0); n.terminate(1);\'')
	print("Wait 60 sec then other run")
	time.sleep(20)