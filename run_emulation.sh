#!/bin/bash
# faith in God
# script to start emulation tests

run_command(){
	# first argument: node name
	# second argument: command to be run
	vcmd -c  "/tmp/$(ls /tmp/ | grep pycore)/$1" -- ${@:2}
}

echo "[+] Waiting for session to begin"
# loop untils there is soment inside the folder pycore
until [[ $(ls /tmp/$(ls /tmp/ | grep pycore) | wc -l )  -gt 1  ]]; do
	sleep 1
done

# exited loop, CORE session began
echo "[+] Session started"
echo "[+] Waiting for routing tables to be set"

# tries to ping router
run_command v10 ping -c 1 192.168.0.1  
until [[ $?  -eq 0  ]]; do
	run_command v10 ping -c 1 192.168.0.1
done

# exited loop, routing tables set
echo "[+] Routing tables set"

cp run_test.py "/tmp/$(ls /tmp/ | grep pycore)/a1.conf"
run_command a1 python3 run_test.py