#!/usr/bin/env python
#-*-coding: utf-8-*
# thanks God
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # supressing warnings
from scapy.all import *

# The ACS server will maintain a secondary long term ARP cache table.
arp_cache = { }

# Function to apply to every packet that arrives
def pktCallback(pkt):
    if pkt.op == 28 and p.hwdst == "ff:ff:ff:ff:ff:ff":
        arp_cache[pkt.psrc] = pkt.hwsrc
        print str(arp_cache)
        print "[+] ACS arp cache updated"

# When a client node joins the network and broadcast a request for ACS, the ACS will reply back with its IP and MAC address.
def listen():
    sniff(iface="wlan0", prn=pktCallback, filter="arp", store=0)

while True:
    listen()