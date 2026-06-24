from socket import *

#connect to server
serverName = 'Yohanna'
serverPort = 12000

#create client socket
ClientSocket = socket(AF_INET, SOCK_STREAM)

#connect to server
ClientSocket.connect((serverName, serverPort))

#send message to server
sentence = input('Input lowercase sentence: ')
ClientSocket.send(sentence.encode())

#penerimaan balsan dari server
modifiedSentence = ClientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())   

#close the socket
ClientSocket.close()
