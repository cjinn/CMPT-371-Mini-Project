Mini Project (25 Points)

Available: Nov 14, 2019
Due Date: Nov 28, 2019
 

In this Mini Project you will practice applying your Socket Programming knowledge to build a simple web server. You will practice

- Socket Programming
- HTTP
- Connection Management
For the first part of your mini project, using Webserver-skeleton.py file, create your simple web server. The missing parts of the code are marked with #Fill in comments, with additional comments on the expected behaviour. Your web server will handle one HTTP request at the time, and implements only the "200 OK" and "404 Not Found" messages to the client (15 points).

To test your web server, copy test-1.html in the same directory of your web server. Then find out the IP address of your machine, and port used in the code for web server and type the following in your web browser: http://IP_ADDRESS:PORT/test.htmlLinks to an external site.

Given web server skeleton can only handle one HTTP request at a time. For the second part of your mini project, implement a multi-threaded version of your web server, capable of handling multiple requests simultaneously. You can implement this with your main thread listening for clients at a fixed port. When your server receives a TCP connection request from a client, the TCP connection to serve the client should happen through another port. Each TCP connection requested is handled in a separate thread. Include your code, and your test procedures in your response. (10 points).

Please submit your mini project in zip format (of your code, and test files), before the midnight on Nov 28, 2019 on the canvas system Mini-Project activity.
