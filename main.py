import os
from clear import clear

pwd = "E:\\Project"
os.chdir(pwd)

clear()

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
    if ch == 'Q':
        break
    choice = {
        'A': "HelloA",
        'B': "HelloB",
        'C': "HelloC",
        'D': "HelloD",
        'E': "HelloE",
        'F': "HelloF",
        'G': "HelloG",
        'H': "HelloH",
    }
    clear()

    res = choice.get(ch, "Invalid Input\n")
    if "Invalid" in res:
        print(res)

