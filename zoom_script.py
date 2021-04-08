## imports
import os

## variables
counter = 0
increment = 1
total = 100 	##arbitrary number in mem that is overwritten by input
zelist = []

## main loop
    ##Ask for number of entries and record it to total
print("Number of entries ")
total = int(input())  
    ## Below line reads inputs from user using map() function 
zelist = list(map(str,input("\nEnter the usernames seperated by spaces : ").strip().split()))[:total]
    ##Start while loop that lasts for the duration of the number of entries
while counter < total:
        ##set directory to name from list
    directory = zelist[counter]
        ## parent Directory path
    parent_dir = "/Users/asmith/Box/Testing"
        ## create concatenated full path
    path = os.path.join(parent_dir, directory)
        ## create the directory
    os.mkdir(path)  
        ## increment the counter to select next uname from list
    counter = counter + increment
