from socket import *
import threading

def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        f = open(filename[1:])
        outputdata = f.read()

        # kirim header
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # kirim isi file
        connectionSocket.send(outputdata.encode())

        connectionSocket.close()

    except:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.close()

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 6789))
    serverSocket.listen(5)

    print("Server siap di port 6789...")

    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Terhubung dengan:", addr)

        thread = threading.Thread(target=handle_client, args=(connectionSocket,))
        thread.start()

if __name__ == "__main__":
    main()