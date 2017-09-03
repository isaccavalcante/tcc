#!/usr/bin/env python
#-*-coding: utf-8-*
# thanks God
# script for sending a single arp packet, with 'op' field modified
# added option: who-is-acs
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # supressing warnings
from scapy.all import *

# New packet class that inherits ARP
class ModifiedARP(ARP):
    name = "Modified ARP"
    fields_desc = [ XShortField("hwtype", 0x0001),
                    XShortEnumField("ptype",  0x0800, ETHER_TYPES),
                    ByteField("hwlen", 6),
                    ByteField("plen", 4),
                    #ShortEnumField("op", 1, {"who-has":1, "is-at":2, "RARP-req":3, "RARP-rep":4, "Dyn-RARP-req":5, "Dyn-RAR-rep":6, "Dyn-RARP-err":7, "InARP-req":8, "InARP-rep":9}),
                    ARPSourceMACField("hwsrc"),
                    SourceIPField("psrc","pdst"),
                    MACField("hwdst", ETHER_ANY),
                    IPField("pdst", "0.0.0.0") ]
    @classmethod
    def addShortEnumField(cls, name, default, enum):
       cls.fields_desc.append(ShortEnumField(name, default, enum))
    
# adding new option in packet field
ModifiedARP.addShortEnumField("op", 1,
    {"who-has":1, "is-at":2, "RARP-req":3,
    "RARP-rep":4, "Dyn-RARP-req":5, "Dyn-RAR-rep":6,
    "Dyn-RARP-err":7, "InARP-req":8, "InARP-rep":9,
    "who-is-acs":10 })

# building the packet
a = ModifiedARP()
a.pdst = '127.0.0.1'
a.psrc = '127.0.0.1'
a.hwsrc = '08:00:27:1a:c0:78'
a.hwdst = '08:00:27:1a:c0:78'
a.op = 'who-is-acs'

# sending the packet
send(a, verbose=False)
print("[+] 1 packet sent") 
a.pdfdump("Packet Description") # saving to pdf
print("[+] packet description saved")