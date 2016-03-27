from socket import *
serverPort = 12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
	connectionSocket ,addr =serverSocket.accept()
	if addr!=None:
		print(str(addr)+' say hello to you')
	sentence=connectionSocket.recv(1024).decode()
	recvSentence=sentence.upper()
	connectionSocket.send(recvSentence.encode())
	connectionSocket.close()