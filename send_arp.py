#!/usr/bin/env python
#-*-coding: utf-8-*
# thanks God
# script for sending a single arp packet, with 'op' field modified
# added option: who-is-acs
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # supressing warnings
from scapy.all import ARP, send

# building the packet
a = ARP()
a.pdst = '127.0.0.1'
a.fields_desc[4].s2i['who-is-acs'] = 28
a.fields_desc[4].i2s[28] = 'who-is-acs'
a.op = 'who-is-acs'

try:
	# sending the packet
	send(a, verbose=False)
	print("[+] 1 packet sent") 
	a.pdfdump("Packet Description") # saving to pdf
	print("[+] packet description saved")
except Exception, msg:
	print(msg)
