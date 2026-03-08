import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_ROT_RATE, PLAYER_SPEED, PLAYER_KEYBINDS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_ROT_RATE * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[PLAYER_KEYBINDS["rotate_left"]]:
            self.rotate(-dt)
        if keys[PLAYER_KEYBINDS["rotate_right"]]:
            self.rotate(dt)
        if keys[PLAYER_KEYBINDS["move_forward"]]:
            self.move(dt)
        if keys[PLAYER_KEYBINDS["move_backward"]]:
            self.move(-dt)

    def move(self, dt):
        init_vector = pygame.Vector2(0, 1)
        rotation_vector = init_vector.rotate(self.rotation)
        move_vector = rotation_vector * PLAYER_SPEED * dt
        self.position += move_vector