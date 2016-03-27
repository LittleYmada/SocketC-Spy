from socket import *
serverName=input('Please enter the name of the seerver:')
serverPort=12000
while 1:
	clientSocket=socket(AF_INET,SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
	sentence=input('input lowercase sentence please:')
	clientSocket.send(sentence.encode())
	modifiedSentence=clientSocket.recv(1024)
	print ('From server we get:'+modifiedSentence.decode())
	clientSocket.close()