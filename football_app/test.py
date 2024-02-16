import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyApplication(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_startup(self):
        # Always call the parent class's do_startup first
        Gtk.Application.do_startup(self)
        # Application-wide setup (actions, menus, etc.) goes here

    def do_activate(self):
        # This method is called when the application is asked to activate
        window = Gtk.ApplicationWindow(application=self)
        window.set_title("Example Application")
        window.show_all()

if __name__ == "__main__":
    app = MyApplication(application_id='org.example.MyApp')
    app.run()
