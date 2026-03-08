import pygame

from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_ROT_RATE, PLAYER_MAX_SPEED, PLAYER_KEYBINDS, PLAYER_SHOT_SPEED, PLAYER_SHOT_CD_SECONDS, PLAYER_ACCEL, PLAYER_V_DECAY

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown: float = 0

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
        self.shot_cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[PLAYER_KEYBINDS["rotate_left"]]: self.rotate(-dt)
        if keys[PLAYER_KEYBINDS["rotate_right"]]: self.rotate(dt)
        if keys[PLAYER_KEYBINDS["move_forward"]]: self.move(dt)
        if keys[PLAYER_KEYBINDS["move_backward"]]: self.move(-dt)
        if keys[PLAYER_KEYBINDS["shoot"]]: self.shoot()

        if self.velocity.magnitude_squared() > 0:
            self.__decay_velocity(dt)
        if self.velocity.magnitude_squared() > PLAYER_MAX_SPEED ** 2:
            self.velocity.normalize_ip()
            self.velocity *= PLAYER_MAX_SPEED

        self.position += self.velocity * dt

    def __decay_velocity(self, dt):
        decay_vector = self.velocity.normalize() * PLAYER_V_DECAY * dt
        self.velocity -= decay_vector

    def move(self, dt):
        init_vector = pygame.Vector2(0, 1)
        rotation_vector = init_vector.rotate(self.rotation)
        accel_vector = rotation_vector * PLAYER_ACCEL * dt
        self.velocity += accel_vector

    def shoot(self):
        if self.shot_cooldown > 0: return

        shot = Shot(self.position.x, self.position.y)
        init_vector = pygame.Vector2(0, 1)
        rotation_vector = init_vector.rotate(self.rotation)
        rotation_vector *= PLAYER_SHOT_SPEED
        shot.velocity = rotation_vector

        self.shot_cooldown = PLAYER_SHOT_CD_SECONDS