import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "192.168.0.34"
# the port, let's use 5001
port = 8888
# the name of file we want to send, make sure it exists
filename = '/Users/pegah2/Movies/silicon valley/Season 5/Silicon.Valley.S05E08.Fifty-One.Percent.720p.AMZN.WEB-DL.Persian2Movie.Com.mkv'
# get the file size
filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")


# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    for _ in progress:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket

