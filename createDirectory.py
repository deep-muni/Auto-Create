import os
from clear import clear


def createDir():
    clear()
    print("Enter directory name:")
    name = input()
    clear()

    try:
        os.mkdir(name)
        print("Directory created")
    except OSError:
        print("File name should not contain special characters")
    finally:
        os.system("pause")
        clear()
        return
