import arcade
import pymunk
import random
import pygame
import time
from game_object import Asteroid, Ship, Background, Bullet

ASTEROID_RADIUS = 30
SHIP_SIZE = 10
ASTEROID_SPEED = 500

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(fullscreen=True)
        self.space = pymunk.Space()
        self.space.gravity = 0, 0
        self.score = 0
        self.game_over = False
        self.music = "assets/images/Battle Over Coruscant Theme.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)
        self.bullet_sound = pygame.mixer.Sound("assets/images/sho5.mp3")
        self.bullet_sound.set_volume(50)
        self.ship = Ship(self.width // 2, self.height // 2, SHIP_SIZE)
        self.ship_life = 3
        self.max_ship_life = 3
        self.asteroid_bodies = []
        self.background = Background(self.width, self.height)
        self.asteroid_creation_time = 0
        self.asteroid_creation_interval = 0.3
        self.last_shot_time = 0
        self.shot_interval = 0.8
        self.particle_list = []
        self.ship_sprite = arcade.Sprite("assets/images/xwing.png", scale=0.2)
        self.asteroid_sprite = arcade.Sprite("assets/images/asteroid.png", scale=1.0)
        self.bullet_sprite = arcade.Sprite("assets/images/bala.png", scale=0.1)
        self.background_sprite = arcade.Sprite("assets/images/fondo.png", scale=1.0)
        self.bullet_sprites = []
        self.bullet_list = []
        self.particle_duration = 0.5
        self.particle_scale = 1.0

    def setup(self):
        self.score = 0
        self.game_over = False

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
        arcade.draw_text(f"Score: {self.score}", self.width // 2, self.height - 30,
                         arcade.color.WHITE, font_size=24, anchor_x="center", anchor_y="center")
        life_text = f"Life: {self.ship_life}/{self.max_ship_life}"
        arcade.draw_text(life_text, self.width - 10, self.height - 30,
                         arcade.color.WHITE, font_size=24, anchor_x="right", anchor_y="center")
        if self.game_over:
            if self.score >= 15:  # Cambio de aquí
                arcade.draw_text("You Win!", self.width // 2, self.height // 2 - 60,
                                 arcade.color.GREEN, font_size=48, anchor_x="center", anchor_y="center")
            else:
                arcade.draw_text("Game Over", self.width // 2, self.height // 2,
                                 arcade.color.RED, font_size=48, anchor_x="center", anchor_y="center")

    def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x
        self.ship.center_y = y

    def on_key_press(self, key, modifiers):
        current_time = time.time()
        if key == arcade.key.SPACE and not self.game_over and current_time - self.last_shot_time >= self.shot_interval:
            self.last_shot_time = current_time
            bullet = Bullet(self.ship.center_x, self.ship.center_y, self.space)
            self.bullet_list.append(bullet)
            self.bullet_sprites.append(bullet.sprite)
            self.space.add(bullet.body, bullet.shape)
            self.bullet_sound.play()

    import arcade
import pymunk
import random
import pygame
import time
from game_object import Asteroid, Ship, Background, Bullet

ASTEROID_RADIUS = 30
SHIP_SIZE = 10
ASTEROID_SPEED = 500

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(fullscreen=True)
        self.space = pymunk.Space()
        self.space.gravity = 0, 0
        self.score = 0
        self.game_over = False
        self.music = "assets/images/Battle Over Coruscant Theme.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)
        self.bullet_sound = pygame.mixer.Sound("assets/images/sho5.mp3")
        self.bullet_sound.set_volume(50)
        self.ship = Ship(self.width // 2, self.height // 2, SHIP_SIZE)
        self.ship_life = 3
        self.max_ship_life = 3
        self.asteroid_bodies = []
        self.background = Background(self.width, self.height)
        self.asteroid_creation_time = 0
        self.asteroid_creation_interval = 0.3
        self.last_shot_time = 0
        self.shot_interval = 0.8
        self.particle_list = []
        self.ship_sprite = arcade.Sprite("assets/images/xwing.png", scale=0.2)
        self.asteroid_sprite = arcade.Sprite("assets/images/asteroid.png", scale=1.0)
        self.bullet_sprite = arcade.Sprite("assets/images/bala.png", scale=0.1)
        self.background_sprite = arcade.Sprite("assets/images/fondo.png", scale=1.0)
        self.bullet_sprites = []
        self.bullet_list = []
        self.particle_duration = 0.5
        self.particle_scale = 1.0

    def setup(self):
        self.score = 0
        self.game_over = False

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
        arcade.draw_text(f"Score: {self.score}", self.width // 2, self.height - 30,
                         arcade.color.WHITE, font_size=24, anchor_x="center", anchor_y="center")
        life_text = f"Life: {self.ship_life}/{self.max_ship_life}"
        arcade.draw_text(life_text, self.width - 10, self.height - 30,
                         arcade.color.WHITE, font_size=24, anchor_x="right", anchor_y="center")
        if self.game_over:
            if self.score >= 15:
                arcade.draw_text("You Win!", self.width // 2, self.height // 2 - 60,
                                 arcade.color.GREEN, font_size=48, anchor_x="center", anchor_y="center")
            else:
                arcade.draw_text("Game Over", self.width // 2, self.height // 2,
                                 arcade.color.RED, font_size=48, anchor_x="center", anchor_y="center")

    def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x
        self.ship.center_y = y

    def on_key_press(self, key, modifiers):
        current_time = time.time()
        if key == arcade.key.SPACE and not self.game_over and current_time - self.last_shot_time >= self.shot_interval:
            self.last_shot_time = current_time
            bullet = Bullet(self.ship.center_x, self.ship.center_y, self.space)
            self.bullet_list.append(bullet)
            self.bullet_sprites.append(bullet.sprite)
            self.space.add(bullet.body, bullet.shape)
            self.bullet_sound.play()

    def update(self, delta_time):
        if self.game_over:
            return
        self.space.step(delta_time)
        asteroids_to_remove = []
        bullets_to_remove = []
        for asteroid_body in self.asteroid_bodies:
            asteroid_body.position = (asteroid_body.position.x, asteroid_body.position.y - ASTEROID_SPEED * delta_time)
            if asteroid_body.position.y < 0:
                asteroids_to_remove.append(asteroid_body)
            if abs(asteroid_body.position.x - self.ship.center_x) < ASTEROID_RADIUS and \
                    abs(asteroid_body.position.y - self.ship.center_y) < ASTEROID_RADIUS:
                self.ship_life -= 1
                asteroids_to_remove.append(asteroid_body)
                if self.ship_life <= 0:
                    self.game_over = True
        for bullet in self.bullet_list:
            bullet.sprite.center_x = bullet.body.position.x
            bullet.sprite.center_y = bullet.body.position.y
            if bullet.sprite.center_y > self.height:
                bullets_to_remove.append(bullet)
            for asteroid_body in self.asteroid_bodies:
                if abs(asteroid_body.position.x - bullet.body.position.x) < ASTEROID_RADIUS and \
                        abs(asteroid_body.position.y - bullet.body.position.y) < ASTEROID_RADIUS:
                    self.score += 1
                    asteroids_to_remove.append(asteroid_body)
                    bullets_to_remove.append(bullet)
                    if self.score >= 15:
                        self.game_over = True
        for asteroid_body in asteroids_to_remove:
            self.space.remove(asteroid_body, *asteroid_body.shapes)
            self.asteroid_bodies.remove(asteroid_body)
        for bullet in bullets_to_remove:
            self.bullet_list.remove(bullet)
            self.space.remove(bullet.body, bullet.shape)
            bullet.sprite.remove_from_sprite_lists()
        self.asteroid_creation_time += delta_time
        if self.asteroid_creation_time >= self.asteroid_creation_interval:
            asteroid = Asteroid(random.randint(0, self.width), self.height, self.space)
            self.asteroid_bodies.append(asteroid.body)
            self.asteroid_creation_time = 0
        for asteroid_body in self.asteroid_bodies:
            if abs(asteroid_body.position.x - self.ship.center_x) < ASTEROID_RADIUS and \
                    abs(asteroid_body.position.y - self.ship.center_y) < ASTEROID_RADIUS:
                self.game_over = True

    def ship_hit_effect(self):
        def change_color():
            self.ship_sprite.color = arcade.color.RED
        def reset_color():
            self.ship_sprite.color = arcade.color.WHITE
        self.ship_sprite.schedule(change_color, interval=0.1, repeat=5, delay=0)
        self.ship_sprite.schedule(reset_color, interval=0.1, repeat=5, delay=0.5)

    def asteroid_explosion_effect(self, x, y):
        explosion = arcade.FadeParticle(center_x=x, center_y=y, change_alpha=5,
                                        lifetime=random.uniform(0.1, self.particle_duration),
                                        mutation_callback=arcade.random_velocity_spread,
                                        start_alpha=255, end_alpha=0,
                                        start_scale=self.particle_scale, end_scale=0.2)
        self.particle_list.append(explosion)

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()
    pygame.mixer.music.stop()


    def ship_hit_effect(self):
        def change_color():
            self.ship_sprite.color = arcade.color.RED
        def reset_color():
            self.ship_sprite.color = arcade.color.WHITE
        self.ship_sprite.schedule(change_color, interval=0.1, repeat=5, delay=0)
        self.ship_sprite.schedule(reset_color, interval=0.1, repeat=5, delay=0.5)

    def asteroid_explosion_effect(self, x, y):
        explosion = arcade.FadeParticle(center_x=x, center_y=y, change_alpha=5,
                                        lifetime=random.uniform(0.1, self.particle_duration),
                                        mutation_callback=arcade.random_velocity_spread,
                                        start_alpha=255, end_alpha=0,
                                        start_scale=self.particle_scale, end_scale=0.2)
        self.particle_list.append(explosion)

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()
    pygame.mixer.music.stop()
