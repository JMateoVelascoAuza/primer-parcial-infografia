import pymunk
import arcade

ASTEROID_RADIUS = 30
SHIP_SIZE = 10

class Asteroid:
    def __init__(self, x, y, space):
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius=30)
        self.shape.density = 1
        self.shape.friction = 0.5
        self.space = space
        self.space.add(self.body, self.shape)

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
    def __init__(self, x, y, space):
        self.sprite = arcade.Sprite("assets/images/bala.png", scale=0.1)
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = x, y
        self.body.gravity = (0, 0)
        self.radius = 5  # Cambio en el atributo: radius en lugar de shape
        self.shape = pymunk.Circle(self.body, radius=self.radius)
        self.shape.density = 1
        self.shape.friction = 0.5
        self.shape.collision_type = 2
        self.space = space
        self.space.add(self.body, self.shape)
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.body.velocity = (0, 300)