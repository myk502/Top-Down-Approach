from socket import *
serverName = '10.147.143.95'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
	message = raw_input('Input lowercase sentence:')
	clientSocket.sendto(message, (serverName, serverPort))
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print modifiedMessage
clientSocket.close()
