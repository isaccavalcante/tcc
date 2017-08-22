# ASA Algorithm :us:

`If` a host sends an outbound ARP message:
    `If` the ARP message is an outbound `ARP request`:
        `If` the IP address in the outbound `ARP request` corresponds to the gateway's IP address: /* Case 4 */
            ASA broadcasts the outbound `ARP request` to the gateway.
        `Else`,
            ASA reports the outbound `ARP request` to a user of the host.
            `If` source is identified and approved by the user: /* Case 3 */
                ASA broadcasts the outbound `ARP request` to the source.
            `Else`,
                ASA drops the outboound `ARP request`.
    `Else`, `if` the ARP message is an outbound `ARP reply`: /* Cases 2 and 4 */
        ASA broadcasts the outbound ARP Reply. ```/* ASA broadcasts the outbound ARP reply only once within random timeout values in Case 2*/ ```

# Algoritmo ACS 🇧🇷
