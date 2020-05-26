import os
from clear import clear


def angularInit():

    print("Enter project name:")
    name = input()
    clear()

    try:
        os.system("ng new " + name + " --skip-install")
    except OSError:
        print("Please use proper name for the project")
    finally:
        os.system("pause")
        clear()
        return

