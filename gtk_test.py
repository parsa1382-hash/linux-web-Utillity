import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

def image_maker(filename, w, h):
    return Gtk.Image.new_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_scale(filename=filename,width=w,height=h,preserve_aspect_ratio=True))

win = Gtk.Window()

grid = Gtk.Grid()
win.add(grid)

box1 = Gtk.Box()
box1.set_spacing(5)

box2 = Gtk.Box()
box2.set_spacing(5)


image1 = image_maker('/home/parsa/Gtk-MusicPlayer/icons/username.png', 28, 28)

entry1 = Gtk.Entry()
entry1.set_placeholder_text("Username...")
label1 = Gtk.Label(label = 'username')
box1.pack_start(image1, True, True, 0)
box1.pack_start(entry1, True, True, 0)


image2 = image_maker('/home/parsa/Gtk-MusicPlayer/icons/password.png', 28, 28)

#   '/home/parsa/Gtk-MusicPlayer/icons/username.png'

entry2 = Gtk.Entry()
entry2.set_placeholder_text("Password...")
label2 = Gtk.Label(label = 'password')
box2.pack_start(image2, True, True, 0)
box2.pack_start(entry2, True, True, 0)

levelbar = Gtk.LevelBar()
levelbar.set_min_value(0)
levelbar.set_max_value(100)
levelbar.set_value(20)


def loggin(button):
    print("<< {} >> Loggin Successfully !".format(entry1.get_text()))

button = Gtk.Button(label = 'Login')
button.connect("clicked",  loggin)




grid.attach(box1, 0, 0, 1, 1)
grid.attach(box2, 0, 1, 1, 1)
grid.attach(button, 0, 2, 2, 2)
#grid.attach(levelbar, 0, 3, 4, 4)
#grid.attach(image, 0, 4, 3, 3)

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
