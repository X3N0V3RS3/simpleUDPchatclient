#coding: utf-8
#Script Written by X3N0V3RS3
import socket,sys,time,os,threading


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip = "192.168.1.99" #sys.argv[1]
port = 100 #int(sys.argv[2])

#Chat function
def chat():
    text = input("Enter message :")
    msg = (f"{name}: {text}")
    s.sendto(msg.encode("ascii"), (ip,port))
    #recieve full chat
    x = s.recvfrom(999999)
    print(x[0])
    #function recusrion/loop
    chat()
    
 
#function main "
name = input("Enter Name :")
chat()
