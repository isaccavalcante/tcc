#!/usr/bin/env python
#-*-coding: utf-8-*
# thanks God
# script for sending a single arp packet, with 'op' field modified
# added option: who-is-acs
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # supressing warnings
from scapy.all import ARP, send

# When a new node joins the network, it broadcasts a `Who is ACS` request