import pygame
import random
import bin.config as config


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((64, 224, 208))
        self.rect = self.surf.get_rect(
            top=30, left=random.randint(30, config.GAME_WIDTH + 20)
        )
        self.speed = 4
        self.kill_next_frame = False
        self.just_created = True

    def update(self):
        if self.just_created == False:
            if self.kill_next_frame == True:
                self.kill()
            if self.rect.bottom + self.speed > config.SCREEN_HEIGHT - 30:
                self.rect.move_ip(0, (config.SCREEN_HEIGHT - self.rect.bottom) - 30)
                self.kill_next_frame = True
                return
            self.rect.move_ip(0, self.speed)
            return
        self.just_created = False
