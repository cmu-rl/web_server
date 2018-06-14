import sys
import json
import time
import socket
import hashlib

HOST, PORT = "18.206.147.166", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)

# add_user, register a new user, return a dictionary
"""
Typical response of add_user:
{"timestamp": "06_13_16_25_08", "message": "User hello2 has been successfully added!", "error": false}
"""
def add_user(username, email):
    data = {}
    data['cmd'] = 'add_user'
    data['mcusername'] = username
    data['email'] = email

    sock.sendto(bytes(json.dumps(data), "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    feedback = json.loads(received)
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
return feedback
