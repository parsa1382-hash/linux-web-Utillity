import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "109.125.129.142"
# the port, let's use 5001
port = 7070



# create the client socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")


mes = 'hello parsa'
s.send(mes.encode())

f = s.recv(BUFFER_SIZE)
print(f)
##############################################################3
'''g = socket.socket()
g.bind(('192.168.1.4', 7070))
g.listen(5)


client_socket, address = g.accept()

rec = client_socket.recv(BUFFER_SIZE).decode()

f = rec.split(SEPARATOR)'''
