#!/usr/bin/env python
#
# Adapted from a https://pastebin.com/tKJ5q5vb
# And found on https://www.project1999.com/forums/showthread.php?t=303219

import socket
import threading
from time import sleep

FROM_IP = "127.0.0.1"
FROM_PORT = 5999
REPLY_IP = ""
REPLY_PORT = 0
TO_IP = "144.121.19.169"
TO_PORT = 5999
 
from_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
from_sock.bind((FROM_IP, FROM_PORT))
to_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
to_sock.bind(('', 0))
 
def local():
  global REPLY_IP, REPLY_PORT
  while True:
    data, addr = from_sock.recvfrom(4096)
    REPLY_IP, REPLY_PORT = addr
    to_sock.sendto(data, (TO_IP, TO_PORT))
    sleep(0.05)
    print("Sending " + str(len(data)) + " bytes to " + TO_IP + ":" + str(TO_PORT))
 
def remote():
  global REPLY_IP, REPLY_PORT
  while True:
    data, addr = to_sock.recvfrom(4096)
    from_sock.sendto(data, (REPLY_IP, REPLY_PORT))
    sleep(0.05)
    print("Sending " + str(len(data)) + " bytes to " + REPLY_IP + ":" + str(REPLY_PORT))
 
print("Waiting for data on " + FROM_IP + ":" + str(FROM_PORT) + "...")
lt = threading.Thread(target=local, args=())
lt.start()
rt = threading.Thread(target=remote, args=())
rt.start()
while True:
  sleep(0.05)
  pass
