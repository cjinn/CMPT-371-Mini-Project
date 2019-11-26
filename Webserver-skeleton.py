from socket import * 
import sys 

# Create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

#Fill in Start
#TODO: Prepare your server socket


#Fill in End

# Server should be up and running and listening to the incoming connections

while True:
	print('The server is ready to serve...')

	# Set up a new connection from the client
	connectionSocket, addr = #Fill in Start   #Fill in End

	try:
		# Receives the request message from the client
		message = connectionSocket.recv(1024).decode()
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		print ('The HTTP Request:') 
		print message
		filename = message.split()[1]
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		# Store the entire contenet of the requested file in a temporary buffer
		outputdata = f.read()
		#TODO: Send the HTTP response header line to the client
		#Fill in Start
		#Fill in End 
 
		# Send the content of the requested file to the client
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode()) 
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
			#TODO: Send HTTP response message for file not found
			#Fill in Start
			#Fill in End
			# Close the client connection socket
			connectionSocket.close()

serverSocket.close()  
sys.exit()
