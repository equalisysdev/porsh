# Python Open Remote Shell
#
# Licensed under GPL-3
# Dynwares
#
# https://github.com/equalisysdev/PORSH/
#
import os

print("##############################################")
print("#             WELCOME TO PORSH               #")
print("#                                            #")
print("#        Type help for all available         #")
print("#                 commands                   #")
print("#                                            #")
print("##############################################")

while True:
    option = input("> ")

    if(option == "help"):
        
        print("##############################################\n")
        print("Available commands:\n")
        print("help: shows this message")
        print("version: shows version number")
        print("connect: connects to the server")
        print("start_server: starts the local server\n")
        print("exit: exits the program\n")
        print("##############################################")