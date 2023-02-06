import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_LSHIFT,
)
import config


class Player(pygame.sprite.Sprite):
    """
    Player entity class
    """
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((5, 5))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                (config.SCREEN_WIDTH - self.surf.get_width()) / 2,
                (config.SCREEN_HEIGHT - self.surf.get_height()) / 2,
            )
        )

    def update(self, key):
        speed = 6
        if key[K_LSHIFT]:
            speed = 2
        if key[K_UP]:
            self.rect.move_ip(0, -speed)
        if key[K_DOWN]:
            self.rect.move_ip(0, speed)
        if key[K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if key[K_RIGHT]:
            self.rect.move_ip(speed, 0)

        if self.rect.left < 30:
            self.rect.left = 30
        if self.rect.right > 30 + config.GAME_WIDTH:
            self.rect.right = 30 + config.GAME_WIDTH
        if self.rect.top <= 30:
            self.rect.top = 30
        if self.rect.bottom >= config.SCREEN_HEIGHT - 30:
            self.rect.bottom = config.SCREEN_HEIGHT - 30
