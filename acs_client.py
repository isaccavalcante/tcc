#!/usr/bin/env python
#-*-coding: utf-8-*
# thanks God
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # supressing warnings
from scapy.all import ARP, Ether, send

# When a new node joins the network, it broadcasts a `Who is ACS` request.
def sendBroadcast():
    a = ARP()
    a.fields_desc[4].s2i['who-is-acs'] = 28
    a.fields_desc[4].i2s[28] = 'who-is-acs'
    a.op = 'who-is-acs'
    a.hwdst = "ff:ff:ff:ff:ff:ff"
    send(a)

sendBroadcast()