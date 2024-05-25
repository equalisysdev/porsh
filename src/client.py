import socket
import os
import subprocess
import sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = 8022
BUFFER_SIZE = 1024 * 512 # 512Kb max size of messages
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"