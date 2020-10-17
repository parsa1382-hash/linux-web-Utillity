import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib
import time
import os
import socket
import tqdm

def image_maker(filename, w, h):
    return Gtk.Image.new_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_scale(filename=filename,width=w,height=h,preserve_aspect_ratio=True))

win = Gtk.Window()

grid = Gtk.Grid()
win.add(grid)


def recv():
    SERVER_HOST = '192.168.0.34'
    SERVER_PORT = 8888

    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"

    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen(5)
    print(f"[*] Listeningas {SERVER_HOST}:{SERVER_PORT}")
    client_socket, address = s.accept()
    print(f"[+] {address} is connected.")


    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)

    filename = os.path.basename(filename)
    filesize = int(filesize)

    progress = tqdm.tqdm(range(filesize), f"Receiving {st}", unit="B", unit_scale=True, unit_divisor=1024)

    with open(filename, "wb") as f:
        for _ in progress:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
        f.write(bytes_read)
        progress.update(len(bytes_read))

def sw(switch, state):
    if switch.get_active():
        recv()

switch = Gtk.Switch()
switch.connect("notify::active", sw)
grid.attach(switch, 0, 0, 1, 1)

button = Gtk.Button(label = 'recive')
button.connect('clicked', sw)
#grid.attach(button, 0, 0, 1, 1)

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
