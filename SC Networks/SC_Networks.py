import math
import socket
import time




def server():
    on = True;
    a = socket.socket()
    host = socket.gethostname()
    port = 12345
    a.bind((host,port))


    a.listen(5)
    while True:
        c , addr = a.accept()
        print('Thank you for connecting to', addr)
        while True:
            message = raw_input('Enter message to send to the client:')
            cool = message + ' ' + str(addr)
            c.send(cool)
            print(c.recv(1024))

def client():
    #time.sleep(4)
    print('Thank you for connecting to my server\b')
    my_ip = raw_input("Enter ip address of server")
    print('\n')
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.connect((my_ip, port))
     #ip_see = s.accept()
    while True:
        h = s.recv(1024)
        data = raw_input("Send Something to the server:\n")
        s.send(data + ' from '+ host)
        print('\n')
        if h:
            print(h + '\n')
        elif not h:
            print('There is no data to be recv')
            break



response = raw_input('Would you like server or client s for server c for client \n')
if response.lower() == "c":
    client()
if response.lower() == "s":
    server()

