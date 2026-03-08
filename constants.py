import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
LINE_WIDTH = 2

PLAYER_RADIUS = 20
PLAYER_ROT_RATE = 300
PLAYER_SPEED = 200

PLAYER_KEYBINDS = {
    "rotate_left": pygame.K_a,
    "rotate_right": pygame.K_h,
    "move_forward": pygame.K_d,
    "move_backward": pygame.K_s,
}

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS