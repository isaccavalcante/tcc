# ASA Algorithm :us:

## Pseudo code:
```Python
if a host sends an outbound ARP MESSAGE:
    if the ARP MESSAGE is an outbound ARP REQUEST:
        if the IP ADDRESS in the outbound ARP REQUEST corresponds to the IP ADDRESS of the gateway: # Case 4 
            ASA broadcasts the outbound ARP REQUEST to the gateway.
        else:
            ASA reports the outbound ARP REQUEST to a user of the host.
            if source is identified and approved by the user: # Case 3 
                ASA broadcasts the outbound ARP REQUEST to the source.
            else:
                ASA drops the outboound ARP REQUEST.
    elif the ARP MESSAGE is an outbound ARP REPLY: # Cases 2 and 4 
        ASA broadcasts the outbound ARP REPLY. # ASA broadcasts the outbound ARP reply only once within random timeout values in Case 2

elif a host receives an inbound ARP MESSAGE:
    if the ARP MESSAGE is an inbound ARP REQUEST:
        if the IP-MAC pair in the ARP REQUEST corresponds to the IP-MAC pair of the gateway registered in ASA-protected host: # Case 4
            ASA broadcasts an outbound ARP REPLY to the gateway,
            and it inserts the IP-MAC pair into ARP cache entries.
        else: # Case 2
            ASA drops the inbound ARP REQUEST,
            and it broadcasts an outbound ARP REPLY to the source of the inbound ARP REQUEST.
    elif the ARP MESSAGE is an inbound ARP REPLY:
        if the IP ADDRESS in the inbound ARP REPLY corresponds to the IP-MAC pair of the gateway registered in ASA-protected host: # Case 4
            ASA inserts the IP-MAC pair of the inbound ARP REPLY into ARP cache entries.
        if the IP ADDRESS in the inbound ARP REPLY corresponds to the IP ADDRESS of the outbound ARP REQUEST sent by an ASA-protected host: # Case 3
            ASA inserts the IP-MAC pair of the inbound ARP REPLY into ARP cache entries.
        else:
            ASA drops the inbound ARP REPLY.
```

# Algoritmo ASA 🇧🇷
