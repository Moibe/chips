#!/bin/bash
#Si está vacía entonces:
timestamp1=$(date +"%d-%m-%Y %H:%M:%S")
echo "$timestamp1 - ATENCIÓN: No se encontró ningún proceso escuchando en el puerto 7880. Reactivando aplicación."
#Reiniciando proceso
cd
cd chips/
source venv/bin/activate
cd sulku-quota
python updateQuota.py &
nuevo_proceso=$(pgrep -f "python updateQuota.py")
timestamp2=$(date +"%d-%m-%Y %H:%M:%S")
echo "$timestamp2 - READY: Quota aumentada en 5 con id $nuevo_proceso. "
.