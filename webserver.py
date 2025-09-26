#import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
serverPort = 6789                     # You can change this port number if needed
serverSocket.bind(('', serverPort))   # '' means accept connections from any address
serverSocket.listen(1)                # Listen for 1 connection at a time
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    # Fill in end

    try:
        # Fill in start
        message = connectionSocket.recv(1024).decode()  # Receive request from browser
        # Fill in end

        filename = message.split()[1]   # Get file name from request
        f = open(filename[1:])          # Remove '/' at the beginning
        # Fill in start
        outputdata = f.read()           # Read file contents
        # Fill in end

        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
