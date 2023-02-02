import pygame
import sys
from entities.Bullet import Bullet
from entities.Player import Player
import config

from pygame.locals import (
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
)

class States():
    """ 
    Base class for game state
    """
    def __init__(self):
        self.done = False    # is the game state finished
        self.next = None     # which state comes next
        self.previous = True # which state came before
        self.quit = False    # should the game quit

class MainMenu(States):
    """
    Main Menu Class
    """
    def __init__(self):
        super().__init__()
        self.next = 'game'
        self.name = 'main_menu'
    
    def cleanup(self):
        print("cleaning up menu state")
    
    def startup(self):
        print('starting up menu state')

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                print('escape pressed')
            if event.key == K_RETURN:
                self.done = True

    def update(self, screen):
        self.draw(screen)
    
    def draw(self, screen):
        screen.fill((0,255,0))

class Game(States):
    """
    Game Class
    """
    def __init__(self):
        super().__init__()
        self.next = 'main_menu'
        self.name = 'game'

    def cleanup(self):
        print("Cleaning up game state")
    
    def startup(self):
        print("starting up game state")

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                print('escape pressed')
            if event.key == K_RETURN:
                self.done = True
    
    def update(self, screen):
        self.draw(screen)
    
    def draw(self, screen):
        screen.fill((255,0,0))

     

def paused() -> None :
    """
    Pauses the game while in a level 
    """
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = False
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()



def main():
    pygame.init
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    state_dict = {
        'main_menu': MainMenu(),
        'game': Game()
    }

    current_state = state_dict['main_menu']

    while current_state.quit == False:

        if current_state.done == True:
            previous, new_state_name = current_state.name, current_state.next
            current_state.cleanup()
            current_state = state_dict[new_state_name]
            current_state.done = False
            current_state.startup()
            current_state.previous = previous
        
        while current_state.done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    current_state.quit = True
                    current_state.done = True
                current_state.get_event(event)
            
            current_state.update(screen)
            pygame.display.update()

            

    
    current_state.cleanup()
    pygame.quit()
    sys.exit()


    # ADDBULLET = pygame.USEREVENT + 1
    # pygame.time.set_timer(ADDBULLET, 40)

    # player = Player()
    # # sprite groups
    # bullets = pygame.sprite.Group()
    # all_sprites = pygame.sprite.Group()
    # all_sprites.add(player)

    # running = True

    # while running:
    #     for event in pygame.event.get():
    #         if event.type == KEYDOWN:
    #             if event.key == K_ESCAPE:
    #                 paused()
    #         if event.type == pygame.QUIT:
    #             running = False

    #         if event.type == ADDBULLET:
    #             new_bullet = Bullet()
    #             bullets.add(new_bullet)
    #             all_sprites.add(new_bullet)

    #     # logic

    #     pressed_keys = pygame.key.get_pressed()
    #     player.update(pressed_keys)

    #     bullets.update()

    #     if pygame.sprite.spritecollideany(player, bullets):
    #         player.kill()
    #         running = False

    #     # graphics
    #     screen.fill((0, 0, 0))
    #     play_area = pygame.Surface((config.GAME_WIDTH, config.GAME_HEIGHT))
    #     play_area.fill((255, 255, 255))
    #     screen.blit(play_area, (30, 30))

    #     for entity in all_sprites:
    #         screen.blit(entity.surf, entity.rect)

    #     pygame.display.flip()



if __name__ == "__main__":
    main()
