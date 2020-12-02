import pyglet, json
import numpy as np

def sacarFormula(): # sacar los valores de a, b, c , d, considerando coordenadas
    with open('data.json') as json_file:
        data = json.load(json_file)

        p = np.polyfit(data["formula"]['X'], data["formula"]['Y'],3)

        f = np.poly1d(p)

    return f

class carritoClass:
    acceleration = 0
    angularVel = 0
    vel = 0
    pos = [0,0]
    angle = 0
    time = 0.02

    def __init__(self):
        self.carritoIMG = pyglet.image.load('assets/carrito.png')
        self.carritoIMG.anchor_x = self.carritoIMG.width // 2 
        self.carritoIMG.anchor_y = self.carritoIMG.height // 2 
        self.sprite = pyglet.sprite.Sprite(self.carritoIMG, x=50, y=50)
        self.label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x = window.width - 200, y = window.height - 50,
                          anchor_x='center', anchor_y='center')
        self.label2 = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x = window.width - 300, y = window.height - 100,
                          anchor_x='center', anchor_y='center')
        
        self.label3 = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x = window.width - 300, y = window.height - 150,
                          anchor_x='center', anchor_y='center')

        self.label4 = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x = window.width - 300, y = window.height - 200,
                          anchor_x='center', anchor_y='center')
    
    def changeAcceleration(self, desired):
        self.acceleration = desired

    def changeStirr(self, desired):
        self.angularVel = desired

    def calculateAll(self):
        if self.vel > 0:
            self.vel += self.acceleration * self.time - self.vel ** 2 / 40000
        else:
            if self.acceleration > 0:
                self.vel += self.acceleration * self.time - self.vel ** 2 / 40000

        self.pos[0] += np.cos(np.radians(-self.angle)) * self.vel
        self.pos[1] += np.sin(np.radians(-self.angle)) * self.vel
        self.angle += self.angularVel * self.vel
        self.sprite.position = (self.pos[0] * scale + offset[0], self.pos[1] * scale + offset[1])
        self.sprite.rotation = self.angle

    def draw(self):
        self.sprite.draw()
        self.label.text = f'vel: {self.vel * 3.6 :.2f} km/h'
        self.label2.text = f'pos: x{self.pos[0] :.2f}, y{self.pos[1] :.2f}'
        self.label3.text = f'perdida de energia: {(self.vel ** 2 / 40000) * 740 * self.vel:.2f} J'
        self.label4.text = f'poder: {self.acceleration * 740 * self.vel:.2f} J'
        self.label.draw()
        self.label2.draw()
        self.label3.draw()
        self.label4.draw()

# start of pyglet!!!
window = pyglet.window.Window(fullscreen = True)

# batches
lineBatch = pyglet.graphics.Batch()

elCoche = carritoClass()

# data
formula = sacarFormula()

with open('data.json') as json_file:
    data = json.load(json_file)
    calleX = np.linspace(data["formula"]['X'][0],data["formula"]['X'][-1], 50)
    calleY = formula(calleX)

# crear las lineas
offset = (10,window.get_size()[1] / 2 - 225)
scale = window.get_size()[1] / 3600

track = []

for i in range(len(calleX)-1):
    track.append(pyglet.shapes.Line((calleX[i]) * scale + offset[0], (calleY[i]) * scale + offset[1], (calleX[i + 1]) * scale + offset[0], (calleY[i + 1]) * scale + offset[1], 5, color = (225, 225, 225), batch = lineBatch))

track.append(pyglet.shapes.Line((calleX[0]) * scale + offset[0], (calleY[0]) * scale + offset[1], (calleX[0]) * scale + offset[0], window.get_size()[1], 5, color = (145, 55, 31), batch = lineBatch))
track.append(pyglet.shapes.Line((calleX[-1]) * scale + offset[0], (calleY[-1]) * scale + offset[1], (calleX[-1]) * scale + offset[0], 0, 5, color = (145, 55, 31), batch = lineBatch))

@window.event
def on_draw():
    window.clear()
    lineBatch.draw() 
    elCoche.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.W:
        elCoche.changeAcceleration(11)
    if symbol == pyglet.window.key.S:
        elCoche.changeAcceleration(-20)

    if symbol == pyglet.window.key.A:
        elCoche.changeStirr(-0.3)
    if symbol == pyglet.window.key.D:
        elCoche.changeStirr(0.3)

@window.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.W:
        elCoche.changeAcceleration(0)
    if symbol == pyglet.window.key.S:
        elCoche.changeAcceleration(0)

    if symbol == pyglet.window.key.A:
        elCoche.changeStirr(0)
    if symbol == pyglet.window.key.D:
        elCoche.changeStirr(0)

def updatePos(rm):
    elCoche.calculateAll()

pyglet.clock.schedule_interval(updatePos, elCoche.time) 

pyglet.app.run()