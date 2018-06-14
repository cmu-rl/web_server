import sys
import json
import time
import socket
import hashlib

HOST, PORT = "18.206.147.166", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)
def add_to_queue(username, email):
    data = {}
    data['cmd'] = 'add_to_queue'
    data['uid'] = username
    data['email'] = email
    sock.sendto(bytes(json.dumps(data), "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    feedback = json.loads(received)
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
return feedback 
