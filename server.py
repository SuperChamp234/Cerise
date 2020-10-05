#!/usr/bin/python3

import socket
import time

defDict = {
    "Zain": "SuperChamp234"
}

def reqHandler(req, clientsocket) :
    if(req[0]=="GET") :
        try :
            print("Request GET %s" %req[1])
            msg = "ANSWER "+str(defDict[req[1]]) + "\n"
            clientsocket.send(msg.encode('ascii'))
        except :
            msg = "ERROR Can't find " + req[1] + "\n"
            clientsocket.send(msg.encode('ascii'))
        return 0
    elif(req[0] == "CLOSE") :
        clientsocket.close()
        return 1
    else :
        return 0
        
            
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostname ="localhost" #socket.gethostname()
port = 9999
server_socket.bind((hostname, port))

server_socket.listen(5)

while True :
    clientsocket, addr = server_socket.accept()
    print("Accepted connection from %", addr)
    while True :
        raw_req = clientsocket.recv(1024)
        req = raw_req.decode('ascii').split(' ')
        req[1] = str(req[1].rstrip("\n"))
        handle = reqHandler(req, clientsocket)
        if(handle == 1) :
            break
server_socket.close()
exit(0)