import pymyip 
import socket
import getpass
import sys
import telnetlib

localhostIP = socket.gethostbyname(socket.gethostname())
print("localhost   -  " + localhostIP + '\n')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIP = s.getsockname()[0]
print("local ip    -  " + localIP + '\n')

externalIP = pymyip.get_ip()
print('external ip -  ' + externalIP + '\n')
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
