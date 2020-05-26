import os
from clear import clear
from createAngular import angularInit
from createDirectory import createDir
from createNode import nodeInit
from createReact import reactInit
from selectDirectory import selectDir

pwd = "E:\\Project"
os.chdir(pwd)

clear()
print("Current Directory >", pwd, "\n")

while True:
    print("What operation you want to perform?: \n"
          "\nA. Select Directory"
          "\nB. Create Directory"
          "\nC. Create Node Project"
          "\nD. Create Angular Project"
          "\nE. Create React Project"
          "\nF. Build Angular Project"
          "\nG. Build React Project"
          "\nH. Git Integration"
          "\n\nq: Quit\n"
          "\nEnter your choice:")

    ch = input().upper()
    if ch == 'A':
        selectDir(pwd)
    elif ch == 'B':
        createDir()
    elif ch == 'C':
        nodeInit()
    elif ch == 'D':
        angularInit()
    elif ch == 'E':
        reactInit()
    elif ch == 'Q':
        break
    else:
        print("Invalid Input")
