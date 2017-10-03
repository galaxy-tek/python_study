##server.py

#import socket sys
import socket
import sys

# create a socket
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

#get the local host address
host = socket.gethostname()

port = 7005
i = 0 
#
serversocket.bind((host, port))

#
serversocket.listen(5)

while True:
	#
	clientsocket,addr = serversocket.accept()  
	print("connect address : %s" % str(addr))
#	while True:
#		data = serversocket.recv(1024)
#		print(data)
	i=i+1
	msg='welcome my first socket '+ "\r\n" + str(i)
	clientsocket.send(msg.encode('utf-8'))
clientsocket.close()
 