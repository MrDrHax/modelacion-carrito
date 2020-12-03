import pyglet
from pyglet.window import key
from pyglet.gl import glTranslatef  

def movement(keys):
    if keys[key.I]:
        glTranslatef(0,10,0)
    if keys[key.K]:
        glTranslatef(0,-10,0)
    if keys[key.J]:
        glTranslatef(-10,0,0)
    if keys[key.L]:
        glTranslatef(10,0,0)

def update(dt):
    window.clear()
    label.draw()
    movement()

if __name__ == '__main__':

    window = pyglet.window.Window(height=1000,width=1000)
    keys = key.KeyStateHandler()
    window.push_handlers(keys)
    label = pyglet.text.Label('Hello, world',
                          font_size=36,
                          x=window.width//2, y=window.height//2)

    pyglet.clock.schedule_interval(update,1/60)
    pyglet.app.run()