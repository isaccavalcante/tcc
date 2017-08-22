# ASA Algorithm :us:

## Pseudo code:
```Python
if a host sends an outbound ARP message:
    if the ARP message is an outbound "ARP request":
        if the IP address in the outbound "ARP request" corresponds to the gateway's IP address: # Case 4 
            ASA broadcasts the outbound "ARP request" to the gateway.
        else,
            ASA reports the outbound "ARP request" to a user of the host.
            if source is identified and approved by the user: # Case 3 
                ASA broadcasts the outbound "ARP request" to the source.
            else,
                ASA drops the outboound "ARP request".
    else, if the ARP message is an outbound "ARP reply": # Cases 2 and 4 
        ASA broadcasts the outbound ARP Reply. # ASA broadcasts the outbound ARP reply only once within random timeout values in Case 2 


```

# Algoritmo ACS 🇧🇷
