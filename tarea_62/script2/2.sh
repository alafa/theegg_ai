#! /bin/bash

dir="./wallpapers"

for f in "$dir"/*; do
	gsettings set org.gnome.desktop.background picture-uri file:$f
	sleep 2m
