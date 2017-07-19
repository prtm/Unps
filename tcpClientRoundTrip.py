#!usr/bin/env python2
# client.py  
import socket
import time

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
tm = s.recv(1024)        
rtt_in_ms = round(time.time() - float(tm), 3)
print rtt_in_ms
s.close()

#print("The round trip time is" % rtt_in_ms)
