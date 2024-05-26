# Python Open Remote Shell
#
# Licensed under GPL-3
# Dynwares
#
# https://github.com/equalisysdev/PORSH/
#
import os
import server
VERSION = "0.1"

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
        print("\033[2J")
        print("##############################################\n")
        print("Available commands:\n")
        print("help: shows this message")
        print("version: shows version number")
        print("connect: connects to the server")
        print("start_server: starts the local server\n")
        print("exit: exits the program\n")
        print("##############################################")
    elif(option == "version"):
        print("\033[2J")
        print("PORSH Client and server")
        print(f"Version {VERSION}")
    elif(option == "start_server"):
        chosed_port = input("choose a port (default:8022)")
        if(chosed_port == ""):
            server.run_server(8022)
        else:
            server.run_server(chosed_port)
        