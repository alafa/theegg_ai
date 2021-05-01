#! /bin/bash

echo "Inserta nº de minutos para la cuenta atrás:"
read minutes
seconds=minutes*60
date1=$((`date +%s` + $seconds))

while [ "$date1" -ge `date +%s` ]; do 
  echo -ne "$(date -u --date @$(($date1 - `date +%s` )) +%H:%M:%S)\r"; 
done

poweroff

