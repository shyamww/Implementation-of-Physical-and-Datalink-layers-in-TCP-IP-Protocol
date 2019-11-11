import socket			 
import data_link
import crc
from physical import encode
from error import error_generator
import manchester

key = "1001"
port = 12348

choice=1
file = open('inputfile.txt','r')
inputStrings = []
input_text=''
Data = []
Ans = []
A1 = []

while(choice!=0):
    print("--------------------------------------")
    print("Assignment: TCP-IP Protocol Simulation")
    print("Menu")
    print("Enter 1 to enter data")
    print("Enter 2 to send data")
    print("Enter 3 view sent data")
    print("Enter 4 generate error")
    print("Enter 5 to display status of Data-link layer")
    print("Enter 6 to display status of Physical layer")
    print("Enter 0 to exit")
    print("--------------------------------------")

    choice = input()

    if(choice==1):
    
        input_string = file.read(10)
        while(input_string!=''):
            inputStrings.append(input_string)
            input_text = input_text + input_string
            data = data_link.string_to_binary(input_string)
            tempdata = "01111110" + data_link.string_to_binary(str('127.0.0.1'))
            tempdata = tempdata + data
            tempdata = tempdata + data_link.string_to_binary(str(len(Data)+1)) + "01111110"
            Data.append(tempdata)
            ans = data_link.encodeData(data,key)
            a1=encode(ans)
            ans=error_generator(a1,0)
            A1.append(a1)
            Ans.append(ans)

            input_string = file.read(10)
        data = data_link.string_to_binary(input_text)
        ans = data_link.encodeData(data,key)
        a1=encode(ans)
        ans=error_generator(a1,0)
        print("Data entered from file successfully !")

    if(choice==2):
        s = socket.socket()		
         
        s.connect(('127.0.0.1', port)) 
        s.sendall(ans)
        s.close() 

        print("Data sent successfully !")

    if(choice==3):
        print("Data entered -->")
        print(input_text)

    if(choice==4):
        ans=error_generator(a1,1)
        print("Error generated and data updated successfully !")

    if(choice==5):
        print("Number of frames = " + str(len(inputStrings)))
        for i in range(len(inputStrings)):
            print("Frame " + str(i) + ": " + inputStrings[i] + ' ' + Data[i])

    if(choice==6):
        print("Number of frames = " + str(len(inputStrings)))
        for i in range(len(inputStrings)):
            print("Frame " + str(i) + ": " + inputStrings[i] + ' ' + Ans[i])


#input_string = raw_input("Enter data you want to send->") 

#data =(''.join(format(ord(x), 'b') for x in input_string)) 
#data = data_link.string_to_binary(input_string)
# print data 

# ans = data_link.encodeData(data,key)
# print(ans)
# a1=encode(ans)
# ans=error_generator(a1)
# s.sendall(ans) 
 
#print s.recv(1024) 

#s.close() 
