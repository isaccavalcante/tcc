#!/bin/bash
# faith in God
# script to start communication between Bob and Alice

fuser -k 5000/tcp

cp bob.py "/tmp/$(ls /tmp/ | grep pycore)/Bob.conf"
cp alice.py "/tmp/$(ls /tmp/ | grep pycore)/Alice.conf"

runCommandAlice(){
	vcmd -c  "/tmp/$(ls /tmp/ | grep pycore)/Alice" -- $@
}

runCommandBob(){
	vcmd -c  "/tmp/$(ls /tmp/ | grep pycore)/Bob" -- $@
}

echo "[+] Waiting for session to begin"
# loop untils there is soment inside the folder pycore
until [[ $(ls /tmp/$(ls /tmp/ | grep pycore) | wc -l )  -gt 1  ]]; do
	sleep 1
done

# exited loop, CORE session began
echo "[+] Sessão started"
echo "[+] Waiting for routing tables to be set"

# tries to ping Bob
Bob=192.168.0.3
runCommandAlice ping -c 1 $Bob  &> /dev/null 
until [[ $?  -eq 0  ]]; do
	runCommandAlice ping -c 1 $Bob &> /dev/null 
done

# exited loop, routing tables set
echo "[+] Routing tables set"

echo "[+] Starting communication"

runCommandBob python3 bob.py &
sleep 1
runCommandAlice python3 alice.py 