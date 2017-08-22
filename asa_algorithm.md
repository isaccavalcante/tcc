# ASA Algorithm :us:

## Pseudo code:
```Python
if a host sends an outbound ARP message:
    if the ARP message is an outbound ARP REQUEST:
        if the ip address in the outbound ARP REQUEST corresponds to the gateway's ip address: # Case 4 
            ASA broadcasts the outbound ARP REQUEST to the gateway.
        else:
            ASA reports the outbound ARP REQUEST to a user of the host.
            if source is identified and approved by the user: # Case 3 
                ASA broadcasts the outbound ARP REQUEST to the source.
            else:
                ASA drops the outboound ARP REQUEST.
    elif the ARP message is an outbound ARP REPLY: # Cases 2 and 4 
        ASA broadcasts the outbound ARP Reply. # ASA broadcasts the outbound ARP reply only once within random timeout values in Case 2 


```

# Algoritmo ACS 🇧🇷
