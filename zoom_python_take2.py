## imports
import os

## variables
counter = 0
increment = 1
total = 100 	##arbitrary number in mem that is overwritten by input

## main list setup
print("Insert unames one per line, using control+d to end ")
zelist = [input()]

## initial directory information
    # Directory
directory = "ZoomUserFolders"
    # Parent Directory path
parent_dir = "/home/asmith/Box/Testing"
    # Path
path = os.path.join(parent_dir, directory)
# Create the directory
os.mkdir(path)

## main loop
print("Number of entries entered above ")
total = int(input())
while counter < total:
    os.mkdir(zelist[counter])
    counter = counter + increment
