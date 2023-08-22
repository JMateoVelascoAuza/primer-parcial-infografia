import arcade
import pymunk
import random
from game_object import Asteroid, Ship, Background, Bullet

ASTEROID_RADIUS = 30
SHIP_SIZE = 10
ASTEROID_SPEED = 100

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(fullscreen=True)
        self.space = pymunk.Space()
        self.space.gravity = 0, -1000
        self.score = 0

        self.ship = Ship(self.width // 2, self.height // 2, SHIP_SIZE)
        self.asteroid_bodies = []
        self.background = Background(self.width, self.height)

        self.asteroid_creation_time = 0
        self.asteroid_creation_interval = 1.0

        self.ship_sprite = arcade.Sprite("assets/images/xwing.png", scale=0.2)
        self.asteroid_sprite = arcade.Sprite("assets/images/asteroid.png", scale=1.0)
        self.bullet_sprite = arcade.Sprite("assets/images/bala.png", scale=0.1)  # Add bullet image
        self.background_sprite = arcade.Sprite("assets/images/fondo.png", scale=1.0)
        self.bullet_sprites = []  # List to store bullet sprites

    def on_draw(self):
        arcade.start_render()
        self.background_sprite.draw()

        self.ship_sprite.center_x = self.ship.center_x
        self.ship_sprite.center_y = self.ship.center_y
        self.ship_sprite.draw()

        for body in self.asteroid_bodies:
            x, y = body.position
            self.asteroid_sprite.center_x = x
            self.asteroid_sprite.center_y = y
            self.asteroid_sprite.draw()

        for bullet_sprite in self.bullet_sprites:
            bullet_sprite.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x
        self.ship.center_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            bullet = Bullet(self.ship.center_x, self.ship.center_y, self.space)
            self.bullet_sprites.append(bullet.sprite)
            self.space.add(bullet.body, bullet.shape)

    def update(self, delta_time):
        self.space.step(delta_time)

        asteroids_to_remove = []
        for body in self.asteroid_bodies:
            body.position = (body.position.x, body.position.y - ASTEROID_SPEED * delta_time)
            if body.position.y < 0:
                asteroids_to_remove.append(body)
        for asteroid_body in asteroids_to_remove:
            self.asteroid_bodies.remove(asteroid_body)
            self.space.remove(asteroid_body, *asteroid_body.shapes)

        bullets_to_remove = []
        for bullet_sprite in self.bullet_sprites:
            bullet_sprite.center_y += 5  # Move bullet vertically
            if bullet_sprite.center_y > self.height:
                bullet_sprite.remove_from_sprite_lists()
                bullets_to_remove.append(bullet_sprite)  # Remove bullet sprites
        for bullet_sprite in bullets_to_remove:
            self.bullet_sprites.remove(bullet_sprite)

        self.asteroid_creation_time += delta_time
        if self.asteroid_creation_time >= self.asteroid_creation_interval:
            asteroid = Asteroid(random.randint(0, self.width), self.height, self.space)
            self.asteroid_bodies.append(asteroid.body)
            self.asteroid_creation_time = 0

        for asteroid_body in self.asteroid_bodies:
            for bullet_sprite in self.bullet_sprites:
                if abs(asteroid_body.position.x - bullet_sprite.center_x) < ASTEROID_RADIUS and \
                        abs(asteroid_body.position.y - bullet_sprite.center_y) < ASTEROID_RADIUS:
                    self.score += 1
                    self.space.remove(asteroid_body, asteroid_body.shapes)
                    self.asteroid_bodies.remove(asteroid_body)
                    bullet_sprite.remove_from_sprite_lists()
                    if self.score % 10 == 0:
                        print("¡La nave ha destruido 10 asteroides!")

if __name__ == "__main__":
    game = MyGame()
    arcade.run()
