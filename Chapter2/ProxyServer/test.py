from socket import *
import sys

if len(sys.argv) <= 1:
    print 'Usage: "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address of the Proxy Server'
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerPort = 8888
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
tcpSerSock.bind(('', tcpSerPort))
tcpSerSock.listen(5)

while True:
    # Start receiving data from the client
    print 'Ready to serve...'
    tcpCliSock, addr = tcpSerSock.accept()
    print 'Received a connection from: ', addr
    message = tcpCliSock.recv(1024)

    # Extract the filename from the given message
    print message.split()[1]
    filename = message.split()[1].partition("/")[2]
    fileExist = "false"
    filetouse = "/" + filename
    try:
        # Check whether the file exists in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        print 'File Exists!'

        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i])
        print 'Read from cache'

        # Error handling for file not found in cache
    except IOError:
        print 'File Exist: ', fileExist
        if fileExist == "false":
            # Create a socket on the proxyserver
            print 'Creating socket on proxyserver'
            c = socket(AF_INET, SOCK_STREAM)

            hostn = filename.replace("www.", "", 1)
            print 'Host Name: ', hostn
            try:
                # Connect to the socket to port 80
                c.connect((hostn, 80))
                print 'Socket connected to port 80 of the host'

                # Create a temporary file on this socket and ask port 80
                # for the file requested by the client 
                fileobj = c.makefile('r', 0)
                fileobj.write("GET " + "http://" + filename + " HTTP/1.0\n\n")

                # Read the response into buffer
                buff = fileobj.readlines() 

                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket
                # and the corresponding file in the cache
                tmpFile = open("./" + filename, "wb")
                for i in range(0, len(buff)):
                    tmpFile.write(buff[i])
                    tcpCliSock.send(buff[i])

            except:
                print 'Illegal request'

        else:
            # HTTP response message for file not found
            # Do stuff here
            print 'File Not Found...Stupid Andy'
            a = 2
    # Close the socket and the server sockets
    tcpCliSock.close()

# Do stuff here
