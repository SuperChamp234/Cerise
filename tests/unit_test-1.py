#!/usr/bin/python3
import socket
import time

def test_get(sock):
    test_msg1 = "GET Zain\n"
    test_msg2 = "GET error\n"
    sock.send(test_msg1.encode("ascii"))
    rply1 = sock.recv(1024)
    if(rply1.decode("ascii") == "ANSWER SuperChamp234\n"):
        print("Test 1 Successful")
    else:
        print("Test 1 Failed")
    sock.send(test_msg2.encode("ascii"))
    rply2 = sock.recv(1024)
    if(rply2.decode("ascii") == "ERROR Can't find error\n"):
        print("Test 2 Successful")
    else:
        print("Test 2 Failed")
    


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "localhost"
port = 9999

sock.connect((host,port))
test_get(sock)
sock.send("CLOSE bye\n".encode("ascii"))
print("Exiting...")
exit(0)