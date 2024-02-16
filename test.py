import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class ImageWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Image Size Example")
        self.set_border_width(10)

        # Load and scale the image
        pixbuf = GdkPixbuf.Pixbuf.new_from_file("path/to/your/image.png")
        scaled_pixbuf = pixbuf.scale_simple(200, 200, GdkPixbuf.InterpType.BILINEAR)  # Desired size

        # Create an image widget with the scaled pixbuf
        image = Gtk.Image.new_from_pixbuf(scaled_pixbuf)

        # Add the image to the window
        self.add(image)

def main():
    win = ImageWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
