import cairocffi as cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 300, 200)
context = cairo.Context(surface)
with context:
    context.set_source_rgb(1, 1, 1)  # White
    context.paint()
# Restore the default source which is black.
context.move_to(90, 140)
context.rotate(-0.5)
context.set_font_size(20)
context.show_text(u'Hi from cairo!')
surface.write_to_png('example.png')

