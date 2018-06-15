# this file containes helper functions to communicate with user server
import sys
import json
import time
import socket
import hashlib

HOST, PORT = "18.206.147.166", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)

def generateUserID(minecraftUUID):
    return hashlib.md5(minecraftUUID.encode('utf-8')).hexdigest()

# add_user, register a new user, return a dictionary
"""
Typical response of add_user:
{"timestamp": "06_13_16_25_08", "message": "User hello2 has been successfully added!", "error": false}
"""
def add_user(username, email):
    data = {}
    data['cmd'] = 'add_user'
    data['uid'] = generateUserID(username) # temporal and buggy
    data['email'] = email

    sock.sendto(bytes(json.dumps(data), "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    feedback = json.loads(received)
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
    return feedback

