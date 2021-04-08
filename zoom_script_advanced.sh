#!/bin/bash

## variables
counter=0
increment=1	
total=100 	##arbitrary number in mem that is overwritten by read

## main array setup
echo 'Insert unames one per line, using control+d to end '
zearray=$(</dev/stdin)	
uname_list=($zearray)

** main loop
cd ~/Box/Testing/test_folder
##cd ~/Box/IT\ Services/zoom_recording_archive
read -p 'Number of entries entered above' total 
while [ $counter -lt $total ];
do 
	mkdir ${uname_list[$counter]}
	let counter=counter+increment
done

