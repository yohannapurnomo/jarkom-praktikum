from socket import *

#define server port
serverPort = 12000

#Create Socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#Bind Socket to port
serverSocket.bind(('', serverPort))

#Listen for connections
serverSocket.listen(1)  

print("The server is ready to receive (click ctrl +c to stop the server)")


while True:
    #Accept connection from client
    connectionSocket, addr = serverSocket.accept()
    print("Connected by", addr)

    #Receive message from client
    sentence = connectionSocket.recv(2048).decode()
    print("Received from client:", sentence)

    #Convert message to uppercase
    modifiedSentence = sentence.upper()

    #Send modified message back to client
    connectionSocket.send(modifiedSentence.encode())

    #Close the connection socket
    connectionSocket.close()

  

