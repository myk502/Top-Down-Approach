def receiveFromServer():
	msg = clientSocket.recv(1024)
	print msg
	return msg

from socket import *
msg = "What to eat tonight?\r\n"
endmsg = "\r\n.\r\n"
mailServer = 'smtp.163.com'
clientSocket = socket(AF_INET, SOCK_STREAM) # The socket for TCP Connection
clientSocket.connect((mailServer, 25))
recv = receiveFromServer()
if(recv[:3] != '220'):
	print '220 reply not received from server.'
heloCommand = 'HELO fanese\r\n'
clientSocket.sendall(heloCommand)
recv1 = receiveFromServer()
if(recv1[:3] != '250'):
	print '250 reply not received from server.'
#Next,we need to login the server
clientSocket.sendall('auth login\r\n')
receiveFromServer()
clientSocket.sendall('ZmFuZXNlbXlrQDE2My5jb20=\r\n')
receiveFromServer()
clientSocket.sendall('BalaBala\r\n')#The base64 code of your password
receiveFromServer()
# Send mail from command
clientSocket.sendall('mail from: <fanesemyk@163.com>\r\n')
receiveFromServer()
clientSocket.sendall('rcpt to: <525039107@qq.com>\r\n')
receiveFromServer()
clientSocket.sendall('data\r\n')
clientSocket.recv(1024)
clientSocket.sendall('from:fanesemyk@163.com\r\n')
clientSocket.sendall('to:525039107@qq.com\r\n')
clientSocket.sendall('subject:kuku is smart\r\n')
clientSocket.sendall('Content-Type:text/plain\t\n')#WTF?
clientSocket.sendall('\r\n')
clientSocket.sendall(msg)
clientSocket.sendall(endmsg)
receiveFromServer()
clientSocket.sendall('quit\r\n')
receiveFromServer()

