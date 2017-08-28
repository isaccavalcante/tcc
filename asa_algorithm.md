# ASA Algorithm :us:

## Pseudo code:
```Python
if a host sends an outbound arp message:
    if the arp message is an outbound ARP REQUEST:
        if the IP address in the outbound ARP REQUEST corresponds to the IP address of the gateway: # Case 4 
            ASA broadcasts the outbound ARP REQUEST to the gateway.
        else:
            ASA reports the outbound ARP REQUEST to a user of the host.
            if source is identified and approved by the user: # Case 3 
                ASA broadcasts the outbound ARP REQUEST to the source.
            else:
                ASA drops the outboound ARP REQUEST.
    elif the arp message is an outbound ARP REPLY: # Cases 2 and 4 
        ASA broadcasts the outbound ARP REPLY. # ASA broadcasts the outbound ARP REPLY only once within random timeout values in Case 2

elif a host receives an inbound arp message:
    if the arp message is an inbound ARP REQUEST:
        if the IP-MAC pair in the ARP REQUEST corresponds to the IP-MAC pair of the gateway registered in ASA-protected host: # Case 4
            ASA broadcasts an outbound ARP REPLY to the gateway,
            and it inserts the IP-MAC pair into arp cache entries.
        else: # Case 2
            ASA drops the inbound ARP REQUEST,
            and it broadcasts an outbound ARP REPLY to the source of the inbound ARP REQUEST.
    elif the arp message is an inbound ARP REPLY:
        if the IP address in the inbound ARP REPLY corresponds to the IP-MAC pair of the gateway registered in ASA-protected host: # Case 4
            ASA inserts the IP-MAC pair of the inbound ARP REPLY into arp cache entries.
        if the IP address in the inbound ARP REPLY corresponds to the IP address of the outbound ARP REQUEST sent by an ASA-protected host: # Case 3
            ASA inserts the IP-MAC pair of the inbound ARP REPLY into arp cache entries.
        else:
            ASA drops the inbound ARP REPLY.
```

# Algoritmo ASA 🇧🇷

```python
`se` um host envia uma mensagem arp:
    `se` a mensagem arp é uma mensagem de saída ARP REQUEST:
        `se` o endereço IP na mensagem de saída ARP REQUEST corresponde ao endereço IP do gateway: # Caso 4
            ASA envia em broadcast a ARP REQUEST de saída para o gateway.
        `caso contrário`:
            ASA reporta a mensagem ARP REQUEST para um usuário do host.
            `se` a fonte é identificada e aprovada pelo usuário: # Caso 3
                ASA envia em broadcast a mensagem ARP REQUEST para a fonte.
            `caso contrário`:
                ASA derruba a mensagem de saída ARP REQUEST.
    `caso contrário, se` a mensagem ARP é uma mensagem ARP REPLY de chegada: # Casos 2 e 4
        ASA envia em broadcast a mensagem ARP REPLY de saída. # ASA envia em broadcast a mensagem ARP de saída apenas uma vez dentro de valores de timoeut aleatórios no Caso 2.
`caso contrário, se` um host recebe uma mensagem ARP de chegada:
    `se` a mensagen ARP é uma mensagem ARP é uma mensagem ARP REQUEST de chegada:
        `se` o par IP-MAC na mensagem ARP REQUEST corresponde ao par IP-MAC do gateway registrado no host protegido pelo ASA: # Caso 4
            ASA envia em broadcast uma mensagem ARP REPLY de saída para o gateway,
            `e` insere o par IP-MAC dentro das entradas cache do ARP.
        `caso contrário`: # Caso 2
            ASA derruba a mensagem ARP REQUEST de chegada,
            `e` envia em broadcast uma mensagem ARP de saída para a fonte da mensagem ARP REQUEST de chegada
    `caso contrário, se` a mensagem ARP é uma mensagem ARP REPLY de chegada:
        `se` o endereço IP na mensagem ARP de chegada corresponde ao par IP-MAC do gateway registrado no host protegido pelo ASA: # Caso 4
            ASA insere o par IP-MAC da mensagem ARP REPLY de chegada dentro das entradas cache do ARP.
        `se` o endereço IP na mensagen ARP ARP REPLY de chegada corresponde ao endereço IP da mensagem AP REQUEST de saída enviada pelo host protegido pelo ASA: # Caso 3
            ASA insere o par IP-MAC da mensagem ARP REPLY de chegada dentro das entradas cache do ARP.
        `caso contrário`:
            ASA derruba a mensagem ARP REPLY de chegada.

```