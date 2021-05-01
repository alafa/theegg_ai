#! /bin/bash

dir="/usr/share/backgrounds"

while true
	do
	for f in "$dir"/*; do

		if [[($f == *.jpg) || ($f == *.png )]]; then
		
			gsettings set org.gnome.desktop.background picture-uri "file://$f"
			sleep 5
		fi
	done
done

