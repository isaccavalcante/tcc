#!/bin/bash
# faith in God
# script to start emulation tests

if [ "$EUID" -ne 0 ]
  then echo "[-] Need to run as root"
  exit 1
fi

GATEWAY_ADDRESS="192.168.0.1"
EXTERNAL_ADDRESS="192.168.1.10"
RANGE_START=1
RANGE_END=10
ATTACKER=a1
LAST_NODE=n$RANGE_END

run_command(){
	# first argument: node name
	# other arguments: command to be run
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

# last node tries to ping gateweay
run_command $LAST_NODE ping -c 1 $GATEWAY_ADDRESS  &> /dev/null
until [[ $?  -eq 0  ]]; do
	sleep 1
	run_command $LAST_NODE ping -c 1 $GATEWAY_ADDRESS &> /dev/null
done

# exited loop, routing tables set
echo "[+] Routing tables set"

# make all hosts continuously ping server
echo "[+] Starting communication between nodes"
for i in $(seq $RANGE_START $RANGE_END); do
	run_command n$i ping $EXTERNAL_ADDRESS &> /dev/null &
done

time_test(){
	echo "[+] Copying test script to attacker"
	cp run_test.py -v "/tmp/$(ls /tmp/ | grep pycore)/$ATTACKER.conf"

	echo "[+] Running test"
	start=`date +%s.%N`

	run_command $ATTACKER python3 run_test.py

	end=`date +%s.%N`
	runtime=$( echo "$end - $start" | bc -l )
	echo "[+] Time elapsed: $runtime"
}

time_test
