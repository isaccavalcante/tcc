#!/usr/bin/env python
#-*-coding: utf-8-*
# thanks God
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # supressing warnings
from scapy.all import *

# The ACS server will maintain a secondary long term ARP cache table.
arp_cache = { }

class ARP_am(AnsweringMachine):
    function_name = "arp_acs"
    filter = "arp"

    def parse_options(self):
        return True

    def is_request(self, req):
        # return 1 if its a req
        return pkt.op == 28 and pkt.hwdst == "ff:ff:ff:ff:ff:ff"
    
    def make_reply(self, req):
        # return reply for the req
        arp_cache[req.psrc] = req.hwsrc
        print("[+] ACS arp cache updated: \n%s\n" % str(arp_cache))
        reply = ARP()
        reply.op = 2
        reply.hwdst = req.hwsrc
        reply.pdst = req.psrc
        return reply

# Function to apply to every packet that arrives
def pktCallback(pkt):
    if pkt.op == 28 and pkt.hwdst == "ff:ff:ff:ff:ff:ff":     
        arp_cache[pkt.psrc] = pkt.hwsrc
        print("[+] ACS arp cache updated")
        reply = ARP()
        reply.op = 'im-acs'
        reply.hwdst = pkt.hwsrc
        reply.pdst = pkt.psrc
        print reply.pdst
        send(reply)

a = ARP_am()
# When a client node joins the network and broadcast a request for ACS, the ACS will reply back with its IP and MAC address.
while True:
    sniff(iface="wlan0", prn=a.make_reply, filter="arp", store=0)
