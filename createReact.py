import os
from clear import clear


def reactInit():

    print("Enter project name:")
    name = input()
    clear()

    try:
        os.system("npx create-react-app " + name)
    except OSError:
        print("Please use proper name for the project")
    finally:
        os.system("pause")
        clear()
        return

