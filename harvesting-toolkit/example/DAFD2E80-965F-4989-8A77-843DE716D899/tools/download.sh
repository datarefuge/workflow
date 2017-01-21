#!/bin/sh

url=$(awk -F = '{print $1}' url.txt)
mkdir -p data
for i in $(cat paths.txt);
do 
	# echo "${url}${i}"
	wget "${url}${i}" -P ./data
	sleep 2
done