#useful while rebooting multiple devices at once-- monitor all from one shell
from multiping import multi_ping #see install instructions @ https://github.com/romana/multi-ping/
import time

addrs = []
while(True):
	#paste your IP's into IPlist.txt (one per line)(same repository that you are executing script from)
	#this file can be dynamically updated while script is running as hosts list is cleared after each iteration
	f = open('IPlist.txt', 'r')
	hosts = f.read()
	f.close()
	addrs = hosts.split()
	
	responses, no_responses = multi_ping(addrs, timeout=2, retry=3)

	for addr, rtt in responses.items():
	    print("------%s------- is --UP-- in %f seconds!" % (addr, rtt))

	for each in no_responses:
		print("------"+each+"------- is down")
	time.sleep(10)#adjust the stall timer in seconds here if you wish
	print("\n-------------------------------------------------------\n")
	addrs.clear()