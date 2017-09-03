import socket
import pdb

# print(socket.gethostbyaddr("8.8.8.8"))
# print(socket.gethostbyname("www.google.com"))

host = 'localhost'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pdb.set_trace()
addr = (host,5555)
mysock.connect(addr)

try:
    msg = b"hi, this is test\n"
    mysock.sendall(msg)
except socket.errno as e:
    print("Socket error", e)
finally:
    mysock.close()













