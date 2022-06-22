#!/usr/bin/env python3
"""
 _______  ___      _______  ______    _______
|   _   ||   |    |       ||    _ |  |       |
|  |_|  ||   |    |    ___||   | ||  |_     _|
|       ||   |    |   |___ |   |_||_   |   |
|       ||   |___ |    ___||    __  |  |   |
|   _   ||       ||   |___ |   |  | |  |   |
|__| |__||_______||_______||___|  |_|  |___|
 _______  _______  _______  _______    ___   _______  __
|       ||       ||       ||       |  |   | |       ||  |
|  _____||_     _||   _   ||    _  |  |   | |_     _||  |
| |_____   |   |  |  | |  ||   |_| |  |   |   |   |  |  |
|_____  |  |   |  |  |_|  ||    ___|  |   |   |   |  |__|
 _____| |  |   |  |       ||   |      |   |   |   |   __
|_______|  |___|  |_______||___|      |___|   |___|  |__|

THIS PROJECT IS INCOMPLETE!

"""

""" PLEASE USE PYTHON 3.2+"""


import sys, wget, requests, json, os.path, zipfile

"""
if sys.version[0] == "2":
    print("Critical Error! This project requires Python 3.2 or higher")
"""

REPO_URL = "https://<YOURUSERNAME>.github.io/qaepm-de/" # a URL de seu repositório, a estrutura de diretórios segue o README do repositório qaepm-de

ARG_ZERO_IS_PYTHON = True # coloque falso caso voce execute diretamente via ./main.py e não python main.py
"""
if ARG_ZERO_IS_PYTHON == True:
    primaryArg = sys.argv[1]
elif ARG_ZERO_IS_PYTHON == False:
"""
DEV_MODE = False # if the code is being tested via debug, leave this constant as true
def main():
    #print(len(sys.argv))
    if DEV_MODE == True:
        showArgs()
    try:
        if sys.argv[1] != "":
            if sys.argv[1] == "help":
                help()
            elif sys.argv[1] == "fetch-infopkg":
                fetchInfoPkg(sys.argv[2])
            elif sys.argv[1] == "fetch-pkg":
                fetchPkg(sys.argv[2])
        else:
            print("Error, invalid or not arg, try 'qaepm help' without single quotes")
    except IndexError as e:
        if DEV_MODE == True:
            print(f"""[DEV MODE] Error as '{e}' """)
        print("Error, invalid or not arg, try 'qaepm help' without single quotes")

def help():
    helpText = """quick and easy package manager or qaepm

USE:
qaepm -option [param ...]

help [no args] show this list
update [no args] update all packages
fetch-infopkg [pkg name, one only] fetch all info (in infopkg.json) about package
fetch-pkg [pkg name, several allowed] downlaod and install package
remove-pkg [pkg name, several allowed] remove packages from computer
repair-pkg [pkg name, one only] reinstall package
"""
    print(helpText)

def fetchInfoPkg(package):
    try:
        pkgUrl = f"{REPO_URL}pkgs/{package}/info.json"
        jsonPkgInfo = requests.get(pkgUrl).text
        pkgInfo = json.loads(jsonPkgInfo)
        if DEV_MODE == True:
            print(f"[DEV MODE] JSON CONTENT: \n{jsonPkgInfo}")
            print(f"[DEV MODE] JSON CONTENT LOADED:\n{pkgInfo}")
        info = f"""Info of package:
        Package Name: {pkgInfo["pkgName"]}
        Package version: {pkgInfo["pkgVersion"]}
        Modification Date: {pkgInfo["pkgModificationDate"]}
        Package File: {pkgInfo["pkgFile"]}
        Description: {pkgInfo["pkgDescription"]}
        Genre: {pkgInfo["pkgGenre"]}
        Developer: {pkgInfo["pkgDeveloper"]}
        Year Creation: {pkgInfo["pkgYearCreation"]}
        Site of Package: {pkgInfo["pkgSiteUrl"]}
        Site of Developer: {pkgInfo["pkgDevSiteUrl"]}
        """
        print(info)
    except Exception as e:
        if DEV_MODE == True:
            print(f"""[DEV MODE] Error as '{e}' """)
        error = f"""Critical error (110E), see if your internet connection has no errors or if this package '{package}' actually exists or was written correctly
"""
        print(error)
def fetchPkg(package):
    try:
        pkgUrl = f"{REPO_URL}pkgs/{package}/info.json"
        jsonPkgInfo = requests.get(pkgUrl).text
        pkgInfo = json.loads(jsonPkgInfo)
        pkgFileUrl = f"""{REPO_URL}pkgs/{package}/{pkgInfo["pkgFile"]}"""
        #response = requests.head(sys.argv[1], allow_redirects=True)
        file = requests.head(pkgFileUrl, allow_redirects=True)
        fileSize = file.headers.get('content-length', -1)
        print(f"{'Package Size'}: {int(fileSize) / float(1 << 20):.6f} MB")
        yesornot = input(f"Download this package anyway? [Y/n]: ").strip()
        if yesornot == "Y" or yesornot == "y":
            if DEV_MODE == True:
                print(f"[DEV MODE] JSON CONTENT: \n{jsonPkgInfo}")
                print(f"[DEV MODE] JSON CONTENT LOADED:\n{pkgInfo}")
                print(f"[DEV MODE] PACKAGE FILE URL: {pkgFileUrl}")
            print(f"""Try Downloading '{package}'""")
            def bar_custom(current, total, width=80):
                print("Downloading Package: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
            if os.path.isfile(pkgInfo["pkgFile"]):
                print("Your package is already installed (110I), if it's corrupt, use 'repair-pkg', and if it's out of date, use 'update'.")
            else:
                wget.download(pkgFileUrl, bar = bar_custom)
        elif yesornot == "N" or yesornot == "n":
            print("Installation was canceled.")
        else:
            print("Invalid option, installation canceled.")
    except Exception as e:
        if DEV_MODE == True:
            print(f"""[DEV MODE] Error as '{e}' """)
        error = f"""Critical error (110EX), see if your internet connection has no errors or if this package '{package}' actually exists or was written correctly, or if any errors occurred with the package download/installation."""
        print(error)
def showArgs():
    a = 0
    while a < len(sys.argv):
        print(f"[DEV MODE] Arg Number {a}: {sys.argv[a]}")
        a += 1
if __name__ == "__main__":
    main()
else:
    print("Error! this program cannot be used as a module, try again running in the conventional way (150E).")
