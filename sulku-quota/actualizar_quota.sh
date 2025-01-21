#!/bin/bash

# Nombre del archivo
archivo="chips/sulku-quota/quota.txt"

# Leer el número actual del archivo
numero_actual=$(cat "$archivo")

# Sumar 5 cada 5 minutos, es la tasa para PRO, o 1 cada 5 minutos en la tasa normal.
nuevo_numero=$((numero_actual + 5))

# Verificar si el nuevo número es mayor a 1500 y ajustarlo si es necesario
if [ "$nuevo_numero" -gt 1500 ]; then
  nuevo_numero=1500
fi

echo "$numero_actual  --> $nuevo_numero"

# Sobreescribir el archivo con el nuevo número
echo "$nuevo_numero" > "$archivo"
