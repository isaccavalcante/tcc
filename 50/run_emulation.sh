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
run_command v10 ping -c 1 192.168.0.1  &> /dev/null
until [[ $?  -eq 0  ]]; do
	sleep 1
	run_command n50 ping -c 1 192.168.0.1 &> /dev/null
done

# exited loop, routing tables set
echo "[+] Routing tables set"

# make all hosts continuously ping server
echo "[+] Starting communication between nodes"
for i in $(seq 1 50); do
	run_command n$i ping 192.168.1.10 &> /dev/null &
done

time_test(){
	echo "[+] Copying test script to host"
	cp run_test.py -v "/tmp/$(ls /tmp/ | grep pycore)/a1.conf"

	echo "[+] Running test"
	start=`date +%s.%N`

	run_command a1 python3 run_test.py

	end=`date +%s.%N`
	runtime=$( echo "$end - $start" | bc -l )
	echo "[+] Time elapsed: $runtime"
}

time_test