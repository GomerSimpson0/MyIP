import pymyip 
import socket
import getpass
import sys
import telnetlib

localhostIP = socket.gethostbyname(socket.gethostname())
print("\nlocalhost   -  " + localhostIP + '\n')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIP = s.getsockname()[0]
print("local ip    -  " + localIP + '\n')

externalIP = pymyip.get_ip()
print('external ip -  ' + externalIP + '\n')
