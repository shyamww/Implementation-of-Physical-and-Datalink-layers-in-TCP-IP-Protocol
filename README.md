Implementation-of-Physical-and-Datalink-layers-in-TCP-IP-Protocol

--------------------------------------------------------------------------

Files for Submission:

Client.py - Sender side to establish communication between 2 nodes

Server.py - Reciever side to establish communication between 2 nodes

Datalink.py - All functions simulating datalink layer in TCP/IP Protocol

Physical.py - All functions simulating physical layer in TCP/IP Protocol

crc.py, manchester.py, bitstuffing.py - All functions simulating main algorithms on data handling and frame handling, designed for simulation.

error.py - Introduce error in data to simulate error detection in program

inputfile.txt, outputfile.txt - File having paragraphs of text to communicate. Inputfile.txt has text to be sent and Outputfile.txt has recieved text.

--------------------------------------------------------------------------

Menu in program is present in both client as well as server side to make it user-friendly. Press various keys to view different functionalities in program and different stages while transfering data.

Menu for client side is as follows: 
	("Enter 1 to enter data")
	("Enter 2 to send data")
	("Enter 3 view sent data")
	("Enter 4 generate error")
	("Enter 5 to display status of Data-link layer")
	("Enter 6 to display status of Physical layer")

Menu for server side is as follows: 
	("Enter 1 to start recieving")
	("Enter 2 to display recieved message")
	("Enter 3 to show error")
	("Enter 4 to display status of Data-link layer")
	("Enter 5 to display status of Physical layer")
	("Enter 6 to view status of frames recieived")

--------------------------------------------------------------------------

To start program, run python server.py and then python client.py in terminal. Menu will be shown in terminal also. Press 1 in client side to fetch data from inputfile.txt and then press 2 in client side to send data. Press 1 in server side to start recieving. Then press other keys to view status and futrther information and/or Testing of Program.

--------------------------------------------------------------------------

Attached screenshots of running program and all major functionalities provided in program for your reference.

--------------------------------------------------------------------------
