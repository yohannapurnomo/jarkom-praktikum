import sys
from socket import *

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_host, server_port))

request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
clientSocket.send(request.encode())

print("Response dari server:")

while True:
    data = clientSocket.recv(4096)
    if not data:
        break
    print(data.decode(), end="")