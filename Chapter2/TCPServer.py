from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	captialiazedSentence = sentence.upper()
	connectionSocket.send(captialiazedSentence)
	connectionSocket.close()
