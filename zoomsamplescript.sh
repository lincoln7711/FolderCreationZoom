#!/bin/bash

counter=0
increment=1
total=5

uname_list=(asmith jwebb rbeutner jhboiselle etc)
cd ~/Box/test_folder
## Folder to set to cd ~/Box/IT Services/zoom_recording_archive
read -p 'Number of entries ' total 
while [ $counter -lt $total ];
do 
	mkdir ${uname_list[$counter]}
	let counter=counter+increment
done

