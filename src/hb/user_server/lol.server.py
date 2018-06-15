# this file containes helper functions to communicate with user server
import sys
import json
import time
import socket
import hashlib
import urllib.request

HOST, PORT = "18.206.147.166", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)

# get uuid from username
def getUUID(username):
    request = "https://api.mojang.com/users/profiles/minecraft/" + username
    contents = urllib.request.urlopen(request).read()
    print("uuid:", contents)
    return json.loads(contents)
     

# get uid from uuid
def generateUserID(minecraftUUID):
    return hashlib.md5(minecraftUUID.encode('utf-8')).hexdigest()

def add_to_queue(username, email):
    data = {}
    data['cmd'] = 'add_to_queue'
    data['uid'] = generateUserID(username) # temporal and buggy
    data['email'] = email
    sock.sendto(bytes(json.dumps(data), "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    feedback = json.loads(received)
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
    return feedback 

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

# get_status returns a dictionary
'''
typical response of get_status
{"timestamp": "06_08_18_15_09", "banned": false, "awesome": true, 
 "queue_position": 120, "message": "...", "error": false}
'''

def get_status(username):
    data = {}
    data['cmd'] = 'get_status'
    data['uid'] = generateUserID(username) # temporal and buggy
    sock.sendto(bytes(json.dumps(data), "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
    status = json.loads(received)
    return status
