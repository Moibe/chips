#!/bin/bash

#Reiniciando proceso
cd
cd chips/
source venv/bin/activate
cd sulku-quota
python updateQuota.py &
nuevo_proceso=$(pgrep -f "python updateQuota.py")
timestamp2=$(date +"%d-%m-%Y %H:%M:%S")
echo "$timestamp2 - READY: Quota aumentada en 5 con id $nuevo_proceso. "