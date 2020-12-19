import pymyip 
import socket
import getpass
import sys
import telnetlib

localhostIP = socket.gethostbyname(socket.gethostname())
print("localhost   -  " + localhostIP)
print("open ports on localhost: ", end = '')
HOST = localhostIP
for port in range (1,65535):
    try:
        if(telnetlib.Telnet(HOST,port)):
            print(port, end = '  ')
    except ConnectionRefusedError as err:
        print("", end = '')
del HOST
print("\n")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIP = s.getsockname()[0]
print("local ip    -  " + localIP)
print("local open ports: ", end = '')
s.close()
HOST = localIP
for port in range (1,65535):
    try:
        if(telnetlib.Telnet(HOST,port)):
            print(port, end = '  ')
    except ConnectionRefusedError as err:
        print("", end = '')
del HOST
del s
print("\n")

externalIP = pymyip.get_ip()
print('external ip -  ' + externalIP)
print('external open ports: ', end  = '')
HOST = externalIP
for i in range(1,1000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    try:
        con = s.connect((HOST, i))
        print(i, end = '  ')
        con.close()
    except:
        pass
print('')
