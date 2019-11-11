import socket 
import data_link
from physical import encode, decode
from error import error_generator
import manchester
import crc

s = socket.socket() 
print ("Socket successfully created") 
 
port = 12348
s.bind(('', port)) 
print ("socket binded to %s" % (port)) 

s.listen(5) 
print ("socket is listening") 

choice=1
data=''
a1=''
ans=''
temp=''
name=''
datalinkData=''
l=0
SinputStrings = []
Sinput_text=''
SData = []
SAns = []
SA1 = []
# c, addr = s.accept() 
# print('Got connection from', addr) 

while True: 
    while(choice!=0):
        print("--------------------------------------")
        print("Assignment: TCP-IP Protocol Simulation")
        print("Server Side Menu")
        print("Enter 1 to start recieving")
        print("Enter 2 to display recieved message")
        print("Enter 3 to show error")
        print("Enter 4 to display status of Data-link layer")
        print("Enter 5 to display status of Physical layer")
        print("Enter 6 to view status of frames recieived")
        print("Enter 0 to exit")
        print("--------------------------------------")
        
        choice = input()

        if(choice==1):
            file = open('outputfile.txt','a') 
            c, addr = s.accept() 
            print('Got connection from', addr) 
            data = c.recv(1024*1024) 
            datalinkData = data
            if not data: 
                break
            a1=decode(data)        
            key = "1001"
            ans = data_link.decodeData(a1, key) 
            temp = "0" * (len(key) - 1) 
            l=len(a1)
            data = a1[ 0 : 0 + l-3]        
            name = data_link.convert_to_massage(data)
            print("Message recieved successfully !")
            file.write(name) 
            file.close()
            c.close() 
            file = open('outputfile.txt','r')
            Sinput_string = file.read(10)
            while(Sinput_string!=''):
                SinputStrings.append(Sinput_string)
                Sinput_text = Sinput_text + Sinput_string
                Sdata = data_link.string_to_binary(Sinput_string)
                Stempdata = "01111110" + data_link.string_to_binary(str('127.0.0.1'))
                Stempdata = Stempdata + Sdata
                Stempdata = Stempdata + data_link.string_to_binary(str(len(SData)+1)) + "01111110"
                SData.append(Stempdata)
                Sans = data_link.encodeData(Sdata,key)
                Sa1=encode(Sans)
                Sans=error_generator(Sa1,0)
                SA1.append(Sa1)
                SAns.append(Sans)

                Sinput_string = file.read(10)
            Sdata = data_link.string_to_binary(Sinput_text)
            Sans = data_link.encodeData(Sdata,key)
            Sa1=encode(Sans)
            Sans=error_generator(Sa1,0)
            file.close()


        if(choice==2):
            print("Recieved message is: "+name)

        if(choice==3):
            print("Remainder after decoding is->"+ans) 
            if ans == temp: 
                print("No Error")
            else: 
                print("Error")

        if(choice==4):
            l=len(a1)
            print(a1[ 0 : 0 + l-3])

        if(choice==5):
            print(datalinkData)

        if(choice==6):
            print("Number of frames recieved = " + str(len(SData)))
            for i in range(len(SData)):
                print("Frame " + str(i) + ": " + ' ' + SData[i])

        
