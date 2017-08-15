# ACS Algorithm :us:

## Client Side Implementation
1. When a new node joins the network, it broadcasts a `Who is ACS` request.
2. The ACS replies back with its `IP and MAC` address which is then stored in client’s ARP cache (static) and in secondary table.
3. The client monitors its ARP cache for changes. If there is any change in ARP cache of client the change is checked against secondary cache.
4. If the IP-MAC binding is present in secondary cache and it is same as the new IP-MAC binding in ARP table, goto step 3.
5. The client sends a request to ACS for the correct MAC address for the given IP address.
6. The IP-MAC binding replied by the ACS is now stored in the client’s ARP cache as well as secondary cache.

## Server Side Implementation
1. The ACS server will maintain a secondary long term ARP cache table.
2. When a client node joins the network and broadcast a request for ACS, the ACS will reply back with its IP and MAC address.
3. When a client node requests for MAC address of an IP address, the ACS will search for the  binding  in  its secondary ARP table.
4. If the IP-MAC binding is present in its secondary ARP table, it will reply the binding to the client node
5. If the IP-MAC binding is not present, it will broadcast ARP Request for the IP address. The MAC address received by ARP Reply is saved in its secondary ARP table.

# Algoritmo ACS 🇧🇷

## Implementação do Cliente
1. Quando um novo nó se junta à rede, ele envia em broadcast uma requisição `Who is ACS`.
2. O ACS responde com o seu endereço `IP e MAC` o qual é então armazenado na cache ARP do cliente e em uma tabela secundária.
3. O cliente monitora a sua cache ARP para mudanças. Se houver alguma mudança na cache ARP do cliente, a mudança é checada contra a cache secundária.
4. Se a ligação IP-MAC é apresentada na cache secundária e a mesma da nova ligação IP-MAC na Tabela ARP, vá para o passo 3.
5. O cliente envia uma requisição para o ACS para o endereço MAC correto para um dado endereço IP.
6. A ligação IP-MAC respondida pelo ACS é agora armazenada na cache ARP do cliente bem como na cache secundária.

## Implementação do Servidor
1. O servidor ACS vai manter uma tabela cache de ARP de longo termo.
2. Quando um nó cliente se junta à rede e envia em broadcast uma requisição para o ACS, o ACS vai responder de volta com o seu endereço `IP e MAC.`
3. Quando um nó cliente faz uma requisição para um endereço MAC de um endereço IP, O ACS vai buscar pela ligação na sua tabela ARP secundária.
4. Se a ligação IP-MAC estiver presente na tabela ARP secundária, ele vai responder a ligação ao nó cliente.
5. Se a ligação IP-MAC não estiver presente, vai enviar em broadcast a `ARP Request` para o endereço IP. O endereço MAC recebido pelo `ARP Reply` é salvo em uma tabela ARP secundária.
