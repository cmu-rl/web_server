# this file containes helper functions to communicate with user server
import sys
import json
import time
import socket
import hashlib
import urllib.request

HOST, PORT = "52.91.188.21", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)

# get uuid from username
def getUUID(username):
    request = "https://api.mojang.com/users/profiles/minecraft/" + username
    contents = urllib.request.urlopen(request).read()
    str_cont = str(contents, "utf-8")
    d =  json.loads(str_cont)
    # yet to handle invalid minecraft username
    if d["id"] == "": raise Exception("minecraft username does not exist")
    return d["id"]

def generateUserID(minecraftUUID):
    try:
        uid = hashlib.md5(minecraftUUID.encode('utf-8')).hexdigest()
    except:
        raise Exception("minecraft username does not exist")
    return uid

def give_error_feedback():
   feedback = {}
   feedback['error'] = True
   print("not valid minecraft name!!!! T^T")
   return feedback

def verified_mc_user(username):
    try:
        uid = generateUserID(getUUID(username))
    except:
        return False
    return True

def add_to_queue(username, email):
    # first vefiry username is valid
    if not verified_mc_user(username):
        return give_error_feedback()
    # if valid, send to user server
    uid = generateUserID(getUUID(username))
    data = {}
    data['cmd'] = 'add_to_queue'
    data['uid'] = uid
    data['email'] = email
    sock.sendto(bytes(json.dumps(data), "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    feedback = json.loads(received)
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
    return feedback 

# add_user, register a new user, return a dictionary
def add_user(username, email):
    # first vefiry username is valid
    if not verified_mc_user(username):
        return give_error_feedback()
    # if valid, send to user server
    uid = generateUserID(getUUID(username))
    data = {}
    data['cmd'] = 'add_user'
    data['mcusername'] = username
    data['uid'] = uid
    data['email'] = email

    sock.sendto(bytes(json.dumps(data), "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    feedback = json.loads(received)
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
    return feedback

# get_status returns a dictionary
def get_status(username):
    # first vefiry username is valid
    if not verified_mc_user(username):
        return give_error_feedback()
    # if valid, send to user server
    uid = generateUserID(getUUID(username))
    data = {}
    data['cmd'] = 'get_status'
    data['uid'] = uid
    sock.sendto(bytes(json.dumps(data), "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
    status = json.loads(received) 
    return status
