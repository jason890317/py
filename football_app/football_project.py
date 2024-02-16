#!/usr/bin/env python3

import gi
import football_standing
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gio


def set_table(leauge):
    

    
    scrolled_window = Gtk.ScrolledWindow()
    scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    # the first option
    listbox = Gtk.ListBox()
    listbox.set_selection_mode(Gtk.SelectionMode.NONE)
    scrolled_window.add(listbox)
    
    data=football_standing.playball(leauge)
    row = Gtk.ListBoxRow()
    grid = Gtk.Grid()
    label_standing=Gtk.Label()
    label_match=Gtk.Label()
    label_win=Gtk.Label()
    label_draw=Gtk.Label()
    label_lose=Gtk.Label()
    label_pts=Gtk.Label()
    label_last=Gtk.Label()
    label_standing.set_markup("<span font='12'>CLUB</span>")
    label_match.set_markup("<span font='12'>Match</span>")
    label_win.set_markup("<span font='12'>Win</span>")
    label_draw.set_markup("<span font='12'>Draw</span>")
    label_lose.set_markup("<span font='12'>Lose</span>")
    label_pts.set_markup("<span font='12'>Pts</span>")
    label_last.set_markup("<span font='12'>Last 5</span>")
    
    label_standing.set_margin_start(150)
    label_standing.set_margin_end(140)
    
    label_match.set_margin_start(10)
    label_match.set_margin_end(20)
    
    label_win.set_margin_start(18)
    label_win.set_margin_end(20)
    
    label_draw.set_margin_start(20)
    label_draw.set_margin_end(20)
    
    label_lose.set_margin_start(20)
    label_lose.set_margin_end(20)

    label_pts.set_margin_start(30)
    label_pts.set_margin_end(20)
    
    label_last.set_margin_start(50)
    # label_last.set_margin_end(10)
    
    grid.attach(label_standing,0,0,50,6)
    grid.attach(label_match,70,0,5,6)
    grid.attach(label_win,80,0,5,6)
    grid.attach(label_draw,90,0,5,6)
    grid.attach(label_lose,100,0,5,6)
    grid.attach(label_pts,110,0,5,6)
    grid.attach(label_last,120,0,5,6)
    row.add(grid)
    listbox.add(row)
    
    if leauge=="bundesliga":
        n=19
    else:
        n=21

    for j in range(1,n):
        row = Gtk.ListBoxRow()
        grid = Gtk.Grid()
        

        # the first : standing
        label=Gtk.Label()
        label.set_markup("<big>"+str(j)+"</big>")
        label.set_halign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL
        label.set_valign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL
        grid.attach(label,0,0,5,6)
        
        # the second : img
        pixbuf = GdkPixbuf.Pixbuf.new_from_file("./"+leauge+"/"+leauge+"_"+data['name'][j-1]+".png")
        scaled_pixbuf = pixbuf.scale_simple(25, 25, GdkPixbuf.InterpType.BILINEAR)  # Desired size
        image = Gtk.Image.new_from_pixbuf(scaled_pixbuf)
        grid.attach(image,10,0,5,5)
        
        # the third : name
        label=Gtk.Label()
        label.set_markup("<span font='13'>"+data['name'][j-1]+"</span>")
        
        label.set_halign(Gtk.Align.START)  # Other options: END, CENTER, FILL
        label.set_valign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL

        grid.attach(label,20,0,12,6)
        
        # the forth : match
        label=Gtk.Label()
        label.set_markup("<span font='13'>"+data['match'][j-1]+"</span>")
        
        label.set_halign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL
        label.set_valign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL

        grid.attach(label,40,0,5,6)
        
        # the fifth : win
        label=Gtk.Label()
        label.set_markup("<span font='13'>"+data['win'][j-1]+"</span>")
        
        label.set_halign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL
        label.set_valign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL

        grid.attach(label,50,0,5,6)
        
        # the sixth : draw
        label=Gtk.Label()
        label.set_markup("<span font='13'>"+data['draw'][j-1]+"</span>")
        
        label.set_halign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL
        label.set_valign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL

        grid.attach(label,60,0,5,6)
        
        # the seventh : lose
        label=Gtk.Label()
        label.set_markup("<span font='13'>"+data['lose'][j-1]+"</span>")
        
        label.set_halign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL
        label.set_valign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL

        grid.attach(label,70,0,5,6)
        
        # the seventh : pts
        label=Gtk.Label()
        label.set_markup("<span font='13'>"+data['pts'][j-1]+"</span>")
        
        label.set_halign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL
        label.set_valign(Gtk.Align.CENTER)  # Other options: END, CENTER, FILL

        grid.attach(label,80,0,5,6)
        
        
        # the seventh : last 5
        grid_last=Gtk.Grid()
        for i in range(5):
            if data['last'][j-1][i]=='Win':
                pixbuf = GdkPixbuf.Pixbuf.new_from_file("./icon/l5l-w.svg")
            elif data['last'][j-1][i]=='Loss':
                pixbuf = GdkPixbuf.Pixbuf.new_from_file("./icon/l5l-l.svg")
            elif data['last'][j-1][i]=='Draw':
                pixbuf = GdkPixbuf.Pixbuf.new_from_file("./icon/l5l-t.svg")
            scaled_pixbuf = pixbuf.scale_simple(23, 23, GdkPixbuf.InterpType.BILINEAR)  # Desired size
            image = Gtk.Image.new_from_pixbuf(scaled_pixbuf)
            grid_last.add(image)
        
        grid.attach(grid_last,90,0,5,6)

        
        
        grid.set_column_spacing(15)  # Padding between columns
        row.add(grid)
        listbox.add(row)
    
    return scrolled_window



class StackWindow(Gtk.Application):
    def __init__(self,application_id, *args, **kwargs):
        super().__init__(application_id="football_app.py", *args, **kwargs)
        

    def do_startup(self):
        Gtk.Application.do_startup(self)  # Always call the parent class's do_startup()

        # Create actions
        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

        # Set up the application menu
        # Note: Actual menu setup code would go here

    def on_quit(self, action, param):
        self.quit()

    def do_activate(self):
        app_win=Gtk.ApplicationWindow(application=self)
        app_win.set_title("Standing")
        # This method would create and show the application's main window
        app_win.set_border_width(10)
        app_win.set_default_size(400, 600)
        # app_win.set_wmclass("football", "Football")
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        app_win.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)
        
        stack.add_titled(set_table('laliga'), 'Laliga', 'Laliga')
        stack.add_titled(set_table('premier'), 'Premier League', 'Premier Leauge')
        stack.add_titled(set_table('serieA'), 'Serie A', 'Serie A')
        stack.add_titled(set_table('bundesliga'), 'Bundesliga', 'Bundesliga')
        
        
        
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        stack.set_size_request(5, 450)
        # stack_switcher.set_size_request(10,10)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)
        
        
        app_win.show_all()
        

if __name__ == "__main__":
    app = StackWindow(application_id='football_app.py')
    app.run()
