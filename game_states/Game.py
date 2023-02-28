import pygame

from pygame.locals import (
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
)

from entities.Player import Player
from entities.Bullet import Bullet

from game_states import State

import config

class Game(State):
    """
    Game Class
    """
    def __init__(self):
        super().__init__()
        self.next = 'main_menu'
        self.name = 'game'
        self.fps = 60


    def cleanup(self) -> None:
        """
        Cleans up the game state
        """
        print("Cleaning up game state")
    
    def startup(self):
        """
        Initialises the game state
        """
        print("starting up game state")
        # Set up play area
        self.play_area = pygame.Surface((config.GAME_WIDTH, config.GAME_HEIGHT))
        self.play_area.fill((255,255,255))
        # create player and sprite groups
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        # Create user event for adding bullets and bullet sprite group
        self.ADDBULLET = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDBULLET, 40)
        self.bullets = pygame.sprite.Group()

    def get_event(self, event) -> None:
        """
        Event listener
        """
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                print('escape pressed')
                paused()
            if event.key == K_RETURN:
                self.done = True
        if event.type == self.ADDBULLET:
            new_bullet = Bullet()
            self.bullets.add(new_bullet)
            self.all_sprites.add(new_bullet)
        
        pressed_keys = pygame.key.get_pressed()
        self.player.update(pressed_keys)

    def update(self, screen) -> None:
        """
        Non event loop game logic
        """
        self.bullets.update()
        if pygame.sprite.spritecollideany(self.player, self.bullets):
            self.player.kill()
            self.done = True
        self.draw(screen)

    def draw(self, screen) -> None:
        """
        Graphics
        """
        screen.fill((0,0,0))
        screen.blit(self.play_area, (30, 30))
        for entity in self.all_sprites:
            screen.blit(entity.surf, entity.rect)

def paused() -> None :
    """
    Pauses the game
    """
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.time.wait(200)
                    pause = False
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()