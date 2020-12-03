from numpy.lib.function_base import angle
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
    vel = 80
    pos = [0,0]
    angle = 90
    time = 0.02
    buscandoPunto = 49
    distanceThreshhold = 25
    deltaX = 0
    deltaY = 0

    slope = 0
    angleNeededToStirr = 0
    angleNeededNormalized = 0
    distance = 0


    def __init__(self):
        self.carritoIMG = pyglet.image.load('assets/carrito.png')
        self.carritoIMG.anchor_x = self.carritoIMG.width // 2 
        self.carritoIMG.anchor_y = self.carritoIMG.height // 2 
        self.sprite = pyglet.sprite.Sprite(self.carritoIMG, x=50, y=50)
        self.sprite.scale = 0.5

        self.chashIMG = pyglet.image.load('assets/resbalo.png')
        self.chashIMG.anchor_x = self.chashIMG.width 
        self.chashIMG.anchor_y = 0
        self.crashSprite = pyglet.sprite.Sprite(self.chashIMG, x=window.width, y=0)

        self.label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x = window.width - 200, y = window.height - 50,
                          anchor_x='center', anchor_y='center')
        self.label2 = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x = window.width - 50, y = window.height - 100,
                          anchor_x='right', anchor_y='center')
        
        self.label3 = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x = window.width - 50, y = window.height - 150,
                          anchor_x='right', anchor_y='center')

        self.label4 = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x = window.width - 50, y = window.height - 200,
                          anchor_x='right', anchor_y='center')
        
        self.pos = [calleX[-1], -500]
    
    def changeAcceleration(self, desired):
        self.acceleration = desired

    def changeStirr(self, desired):
        self.angularVel = desired

    def getNextPoint(self):
        self.deltaX = (calleX[self.buscandoPunto] - self.pos[0])
        self.deltaY = (calleY[self.buscandoPunto] - self.pos[1])
        self.distance  = self.deltaX**2 + self.deltaY**2 # dejamos la distancia al cuadrado para optimizar, ya que sacar raiz cuadrada es algo que toma muchos recursos

        try: 
            self.slope = self.deltaY/self.deltaX
            self.angleNeededNormalized = np.degrees(np.arctan(self.slope))
            if self.deltaY >= 0:
                if self.deltaX >= 0: # cuadrante 4
                    self.angleNeededNormalized += 180
                else: # cuadrante 3
                    self.angleNeededNormalized += 360
            else:
                if self.deltaX >= 0: # cuadrante 2
                    self.angleNeededNormalized += 180
                else: # cuadrante 1
                    pass
            self.angleNeededToStirr = self.angleNeededNormalized #- self.angle

        except:
            if self.deltaY > 0:
                self.angleNeededToStirr = 270 #- self.angle
            else:
                self.angleNeededToStirr = 90 #- self.angle

        self.angleNeededToStirr = (self.angle) - (self.angleNeededToStirr - 180) # flip
        if self.angleNeededToStirr > 180:
            self.angleNeededToStirr -= 360
        self.changeAcceleration(11)

    def followCurve(self):
        self.getNextPoint()

        if self.distance < self.distanceThreshhold:
            self.buscandoPunto -= 1
            if self.buscandoPunto < 0:
                self.pos = [calleX[-1], -1000]
                self.buscandoPunto = len(calleX)-1
        
        self.changeStirr(-self.angleNeededToStirr/10) 

    def calculateAll(self):
        if self.vel > 0:
            self.vel += self.acceleration * self.time - self.vel ** 2 / 40000
        else:
            self.vel = 0
            if self.acceleration > 0:
                self.vel += self.acceleration * self.time - self.vel ** 2 / 40000

        self.pos[0] += np.cos(np.radians(self.angle)) * self.vel * self.time
        self.pos[1] += np.sin(np.radians(self.angle)) * self.vel * self.time

        # hacemos que el angulo interno simpre este entre el rango de 0 a 360
        if self.angle < 0:
            self.angle += 360
        if self.angle > 360:
            self.angle -= 360
        
        if autoControl:
            self.followCurve()
        self.angle += self.angularVel #* self.vel
        self.sprite.position = (self.pos[0] * scale + offset[0], self.pos[1] * scale + offset[1])
        self.sprite.rotation = -self.angle


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

        if not autoControl:
            self.crashSprite.draw()

# start of pyglet!!!
window = pyglet.window.Window(fullscreen = True)

# batches
lineBatch = pyglet.graphics.Batch()



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

# sprites / shapes
square = pyglet.shapes.Rectangle(0, 0, window.width, window.height, color=(55, 150, 55))

benchesIMG = pyglet.image.load('assets/gradas.jpg')
benchesIMG.anchor_x = benchesIMG.width // 2
benchesIMG.anchor_y = benchesIMG.height // 2
crashSprite = pyglet.sprite.Sprite(benchesIMG, x = (1250) * scale + offset[0], y = (-600) * scale + offset[1], batch = lineBatch)
crashSprite.update(rotation=-30, scale_x=0.3, scale_y=None)

elCoche = carritoClass()

@window.event
def on_draw():
    window.clear()
    square.draw()
    lineBatch.draw() 
    elCoche.draw()

@window.event
def on_key_press(symbol, modifiers):
    global elCoche
    if symbol == pyglet.window.key.W:
        elCoche.changeAcceleration(11)
    if symbol == pyglet.window.key.S:
        elCoche.changeAcceleration(-20)

    if symbol == pyglet.window.key.A:
        elCoche.changeStirr(3)
    if symbol == pyglet.window.key.D:
        elCoche.changeStirr(-3)

    if symbol == pyglet.window.key.SPACE:
        global autoControl
        autoControl = False
        elCoche.changeAcceleration(-20)
        elCoche.changeStirr(0)

    if symbol == pyglet.window.key.R:
        elCoche = carritoClass()
        autoControl = True

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

autoControl = True

def updatePos(rm):
    elCoche.calculateAll()

pyglet.clock.schedule_interval(updatePos, elCoche.time) 

pyglet.app.run()