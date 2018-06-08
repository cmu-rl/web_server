# this file containes helper functions to communicate with user server
import sys
import json
import time
import socket
import hashlib

HOST, PORT = "18.206.147.166", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)

def add_user(username, password):
    data = {}
    data['cmd'] = 'add_user'
    data['mcusername'] = username
    data['email'] = password

    sock.sendto(bytes(json.dumps(data), "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))

def get_status(username, password):
    data = {}
    data['cmd'] = 'get_status'
    data['uid'] = username
    sock.sendto(bytes(json.dumps(data), "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
 
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
