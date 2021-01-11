import socket
import threading

mysocket= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

myip="192.168.43.84"
myport=2323

mysocket.bind((myip,myport))

def recv_data():
    while True:
        x=mysocket.recvfrom(64)
        t=x[1][0]
        t=str(t)
        if t=="192.168.43.122":
            print("Linux_User: ",x[0].decode())
        else:
            print("Redhat_User: ",x[0].decode())

def sends():
    while True:
        server_ip= "192.168.43.190"
        port= 6363
        msg= input()
        mysocket.sendto(msg.encode(), (server_ip, port))
        mysocket.sendto(msg.encode(),("192.168.43.122",1234))

x1= threading.Thread(target=recv_data)
x2= threading.Thread(target= sends)

x1.start()
x2.start()
