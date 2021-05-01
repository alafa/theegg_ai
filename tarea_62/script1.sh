#! /bin/bash

echo "Introduce los minutos max deseados desde la última modificacion"
read max_min

dir="./ficheros"

echo "Threshold is: $max_min minutes"
echo "Estos ficheros fueron modificados por última vez:"
for f in "$dir"/*; do

	minutes_ago=$((($(date "+%s") - $(date -r "$f" "+%s") ) / 60 ))
	f_parts=$(echo $f | tr "/", "\n")
	echo $f": $minutes_ago minutes ago"
	if [ $minutes_ago -gt $max_min ]; then
	
	basename "$f"
	name_file="$(basename -- $f)"
	mv $f $dir/OLD_$name_file
	fi

done

