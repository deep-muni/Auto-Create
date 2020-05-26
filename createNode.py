import os


def nodeInit():

    os.system("npm init --yes")
    file = open("index.js", "w+")
    file.close()
    return
