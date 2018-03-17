#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject
import cairo
import math
import time

def progress_timeout(object):
    w, h = 600, 400
    object.queue_draw()
    return True

def expose(drawingarea, cr):
        # time 

        hours = time.localtime().tm_hour
        minutes = time.localtime().tm_min
        secs = time.localtime().tm_sec
        minute_arc = (2*math.pi / 60) * minutes
        secs_arc = (2*math.pi / 60) * secs
        if hours > 12:
            hours = hours - 12       
        hour_arc = (2*math.pi / 12) * hours + minute_arc / 12
       
        # clock background

        w, h = window.get_size()
        cr.set_source_rgba(1, 0.2, 0.2, 0.6)
        cr.arc(w/2, h/2, min(w,h)/2 - 8 , 0, 2 * 3.14) 
        cr.fill()
        cr.stroke()

        # center arc

        cr.set_source_rgb(1, 0, 0)
        cr.arc ( w/2, h/2, (min(w,h)/2 -20) / 5, 0, 2 * math.pi)
        cr.fill()
        cr.line_to(w/2,h/2)
        cr.stroke()

        # pointer hour

        cr.set_source_rgba(0.5, 0.5, 0.5, 0.5) 
        cr.set_line_width ((min(w,h)/2 -20)/6 )
        cr.move_to(w/2,h/2)
        cr.line_to(w/2 + (min(w,h)/2 -20) * 0.6 * math.cos(hour_arc - math.pi/2),
            h/2 + (min(w,h)/2 -20) * 0.6 * math.sin(hour_arc - math.pi/2))
        cr.stroke()

        # pointer minute

        cr.set_source_rgba(0.5, 0.5, 0.5, 0.5) 
        cr.set_line_width ((min(w,h)/2 -20)/6 * 0.8)
        cr.move_to(w/2,h/2)
        cr.line_to(w/2 + (min(w,h)/2 -20) * 0.8 * math.cos(minute_arc - math.pi/2), 
            h/2 + (min(w,h)/2 -20) * 0.8 * math.sin(minute_arc - math.pi/2))
        cr.stroke()
 
        # pointer second

        cr.set_source_rgba(0.5, 0, 0, 0.9) 
        cr.set_line_width ((min(w,h)/2 -20)/6 * 0.5)
        cr.move_to(w/2,h/2)
        cr.line_to(w/2 + (min(w,h)/2 -20) * 0.9 * math.cos(secs_arc - math.pi/2), 
            h/2 + (min(w,h)/2 -20) * 0.9 * math.sin(secs_arc - math.pi/2))
        cr.stroke()
 

window = Gtk.Window()
window.set_title("Analogue Clock")
window.set_default_size(600, 400)
window.connect("destroy", Gtk.main_quit)

drawingarea = Gtk.DrawingArea()

drawingarea.connect("draw", expose)
window.add(drawingarea)
window.timer = GObject.timeout_add (1000, progress_timeout, window)
window.show_all()

Gtk.main()
