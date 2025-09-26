<img width="759" height="157" alt="image" src="https://github.com/user-attachments/assets/20929b75-a3e4-4800-9a7c-989825db9eb9" />Lab 1: Web Server Lab
In this lab, you will learn the basics of socket programming for TCP connections in Python: how to create
a socket, bind it to a specific address and port, as well as send and receive a HTTP packet. You will also
learn some basics of HTTP header format.
You will develop a web server that handles one HTTP request at a time. Your web server should accept
and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response
message consisting of the requested file preceded by header lines, and then send the response directly to
the client. If the requested file is not present in the server, the server should send an HTTP “404 Not
Found” message back to the client

HOW to run
Run the server by running the file

then get pc ip address and do http://192.168.1.1:6789/HelloWorld.html
and the html should pop up.
have to rerun the code to test the 404 not found
after starting it up run 
http://192.168.1.1:6789/NOFile.html
