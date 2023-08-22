import pymunk

ASTEROID_RADIUS = 30
SHIP_SIZE = 10
ASTEROID_SPEED = 100

class Asteroid:
    def __init__(self, x, y, space):
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, ASTEROID_RADIUS)
        self.shape.density = 1
        self.shape.friction = 0.5
        space.add(self.body, self.shape)

class Ship:
    def __init__(self, x, y, size):
        self.center_x = x
        self.center_y = y
        self.size = size

class Background:
    def __init__(self, width, height):
        self.center_x = width // 2
        self.center_y = height // 2

class Bullet:
    def __init__(self, x, y, velocity):
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, 5)
        self.shape.density = 1
        self.shape.friction = 0.5
        self.velocity = velocity