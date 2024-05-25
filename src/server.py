# Python Open Remote Shell
#
# Licensed under GPL-3
# Dynwares
#
# https://github.com/equalisysdev/PORSH/
#

import socket

# Server host and port
SERVER_HOST = "0.0.0.0"
# Maximum message size (512Kb)
BUFFER_SIZE = 1024 * 512
# Separator sign used to separate results and current working directory
SEPARATOR = "<sep>"

# Create a socket object
s = socket.socket()

def initialize_server(SERVER_PORT=8022):
    """
    Initializes the server by binding it to the specified host and port.
    """
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"Listening on {SERVER_HOST}:{SERVER_PORT}")

def accept_connection():
    """
    Accepts a connection from a client and returns the client socket.
    """
    client_socket, client_address = s.accept()
    print(f"{client_address[0]}:{client_address[1]} Connected!")
    return client_socket


def receive_cwd(client_socket):
    """
    Receives the current working directory from the client.
    """
    cwd = client_socket.recv(BUFFER_SIZE).decode()
    print("[+] Client current working directory:", cwd)
    return cwd

def get_command(cwd):
    """
    Prompts the user for a command and returns it.
    """
    command = input(f"{cwd} $> ")
    return command

def send_command(client_socket, command):
    """
    Sends a command to the client.
    """
    client_socket.send(command.encode())

def receive_output(client_socket):
    """
    Receives the output of a command from the client.
    """
    output = client_socket.recv(BUFFER_SIZE).decode()
    return output

def run_server():
    """
    Runs the server and handles client connections.
    """
    initialize_server()

    while True:
        client_socket = accept_connection()

        cwd = receive_cwd(client_socket)

        while True:
            command = get_command(cwd)

            if command == "exit":
                break

            send_command(client_socket, command)
