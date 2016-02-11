import gtk
from boto.ec2.cloudwatch import MetricAlarm
import classaws
AlarmCatcher = classaws.Alarmgetter()


class CloudWatcher:
    def __init__(self):
        self.tray = gtk.StatusIcon()
        self.tray.set_tooltip("AWS CloudWatcher")
        #self.tray.set_blinking(True)
        self.tray.set_from_stock(gtk.STOCK_ABOUT)
        self.tray.set_from_file("cloudwatch.png")
        self.tray.connect('popup-menu', self.on_right_click)
        self.tray.set_tooltip(('CloudWatcher'))

    def on_right_click(self, icon, event_button, event_time):
        self.make_menu(event_button, event_time)

    def make_menu(self, event_button, event_time):
        menu = gtk.Menu()
        # OK Alarms
        #okalarms = xx.get_OK("amount")
        okalarm = gtk.MenuItem("OK : %d" % AlarmCatcher.get_OK("amount"))
        okalarm.show()
        menu.append(okalarm)
        okalarm.connect('activate', self.myWindow, "showOK")
        ## INSUS Alarms
        insualarm = gtk.MenuItem("INSUFFICIENT : %d" % AlarmCatcher.get_INSU("amount"))
        insualarm.show()
        menu.append(insualarm)
        #insualarm.connect('activate', self.myWindow)
        ## real Alarms
        alalarm = gtk.MenuItem("ALARM : %d" % AlarmCatcher.get_ALARM("amount"))
        alalarm.show()
        menu.append(alalarm)
        #alalarm.connect('activate', self.myWindow)
        #window
        #test = xx.get_OK("amount")
        yps = gtk.MenuItem("hi")
        yps.show()
        menu.append(yps)
        yps.connect('activate', self.myWindow, "lol")
        ## show about dialog
        about = gtk.MenuItem("About")
        about.show()
        menu.append(about)
        about.connect('activate', self.show_about_dialog)
        # add quit item
        quit = gtk.MenuItem("Quit")
        quit.show()
        menu.append(quit)
        quit.connect('activate', gtk.main_quit)
        menu.popup(None, None, gtk.status_icon_position_menu,
                event_button, event_time, self.tray)

    def show_about_dialog(self, widget):
        about_dialog = gtk.AboutDialog()
        about_dialog.set_destroy_with_parent (True)
        about_dialog.set_icon_name ("AWS Cloudwatch Alert Icon")
        about_dialog.set_name('AWS CloudWatcher')
        about_dialog.set_version('0.1')
        about_dialog.set_copyright("(C) Yves Sanderband")
        about_dialog.set_comments(("Show AWS Cloudwatch Alerts in Systray"))
        about_dialog.set_authors(['Yves Sanderbrand <yves.sanderbrand@gmail.com>'])
        about_dialog.run()
        about_dialog.destroy()

    def myWindow(self, window, show):
        #if show == showOK
        win = gtk.Window()
        win.set_default_size(200,100)
        win.set_destroy_with_parent (True)
        win.connect("delete-event", gtk.main_quit)
        win.show_all()

if __name__ == "__main__":
    CloudWatcher()

    gtk.main()
