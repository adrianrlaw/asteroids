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