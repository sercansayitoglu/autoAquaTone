#!/usr/bin/env python3
# version 0.4
# Use domains.cfg as a source to domains. Write them line by line!
# Just fill domains.cfg and run this script in this directory
# just run it, no parameter
# more info github.com/sercansayitoglu


from time import sleep
from subprocess import call, Popen
from os import stat

Popen("echo 1 > engine.cfg",shell=True)  #it will allow while loop to go
Popen("echo ------------------------ >> log.txt",shell=True)
Popen("date | cat >> log.txt",shell=True)
Popen("echo newSessionStarted >> log.txt",shell=True)
call(["clear"])
call(["cat", "banner.txt"])  #I think that's fancy
print ("\n\nLet's check whether the Aquatone has installed or not.\nIf it hasn't, it will be install!")
sleep(.5) #who doesn't like to sleep?
call(["gem", "install", "aquatone"])  # It will try to install aquatone
print ("\n\n\nREADY TO GO!\n\n")
sleeptime = 0     #just for counting, not important
sleeptimerow = 0  #same
while True:    #infinite loop, if engine.cfg is 0 it will stop
	file3 = open("engine.cfg","r")  #read engine
	engine = file3.readline()
	file3.close()
	engine =  engine.replace('\n','')
	engines=False
	if str(engine) == "0":  engines=True #  if  engine is  0 set enginev true
	if engines:  #if engines is true exit while loopp and stop process
		print("engine stop")
		Popen("echo engineStop >> log.txt", shell=True)
		break
	Popen("echo engineStarted >> log.txt",shell=True)
	Popen("date | cat >> log.txt",shell=True)
	statinfo = stat('domains.cfg')  #will get the metadata about domains.cfg
	if statinfo.st_size > 0:    #if domains.cfg is not empty
		print ("\n\n")
		Popen("echo domainCfgisGreaterThenZero >> log.txt",shell=True)
		Popen("date | cat >> log.txt",shell=True)
		sleeptimerow = 0    #reset count
		file = open("domains.cfg","r",encoding = "ISO-8859-1")
		domain = file.readline()    #read next domain from  domains.cfg
		file.close()
		domain = domain.replace('\n','')  # delete unwanted things
		domain = domain.replace(' ','')   # same
		file2 = open("history.cfg","r",encoding = "ISO-8859-1")
		history = file2.readlines()
		file2.close()
		historyv=False
		for line in history:    #purpose: if domain has scanned before don't scan it again
			line = line.replace('\n','')
			if line != '\n' and line == domain:
				historyv=True
		if historyv:
			Popen("echo " + domain + " >> log.txt", shell=True)
			Popen("echo isAlreadyExist >> log.txt", shell=True)
			Popen("date | cat >> log.txt",shell=True)
			Popen("sed -i '1d' domains.cfg", shell=True) # delete the first line of domains.cfg
			continue
		sleep(1)
		print ("Lucky domain is:", domain, "!!!!!")
		Popen("echo " + domain + " >> log.txt", shell=True)
		Popen("date | cat >> log.txt",shell=True)
		sleep(2)
		Popen("echo discoverHasStarted >> log.txt", shell=True)
		Popen("date | cat >> log.txt",shell=True)
		call(["aquatone-discover", "--domain", domain])  #classic aquatone-discover
		Popen("echo takeoverHasStarted >> log.txt", shell=True)
		Popen("date | cat >> log.txt",shell=True)
		call(["aquatone-takeover", "--domain", domain])  #classic aquayone-takeover
		print ("\n\n\nComplete!\n")
		Popen("echo takeoverHasFinished >> log.txt", shell=True)
		Popen("date | cat >> log.txt",shell=True)
		Popen("sed -i '1d' domains.cfg", shell=True) # delete the first line of domains.cfg
		Popen("echo " + domain + " >> history.cfg",shell=True)  #add domain to history.cfg
		sleep(2)
	else:
		print ("\n\n--------\n\ndomains.cfg is empty!\n")   #domain.cfg is empty you have to put somethings in it
		Popen("echo domains.cfgIsEmptyWillWaitFor30Seconds >> log.txt", shell=True)
		Popen("date | cat >> log.txt",shell=True)
		sleeptime += 1
		sleeptimerow += 1
		print ("Program will sleep for ", sleeptime, ". time.",sep='')
		if sleeptimerow > 1:
			print ("Program will sleep ", sleeptimerow, ". time in a row.",sep='')
		else:
			print ("Program will sleep for first time in a row.")
		sleep(0)
		print ("5 seconds more!")
		sleep(5)
