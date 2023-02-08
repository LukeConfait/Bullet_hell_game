
import pygame
import random
import sys

from pygame.locals import (
    K_ESCAPE,
    K_RETURN,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_LSHIFT,
    KEYDOWN,
)

from entities.Bullet import Bullet
from entities.Player import Player
import config

class States():
    """ 
    Base class for game state
    """
    def __init__(self):
        self.done = False      # is the game state finished
        self.next = None       # which state comes next
        self.previous = 'None' # which state came before
        self.quit = False      # should the game quit
        self.fps = 60          # framerate

class MainMenu(States):
    """
    Main Menu Class
    """
    def __init__(self):
        super().__init__()
        self.next = 'game'
        self.name = 'main_menu'
        self.fps = 15
    
    def cleanup(self) -> None:
        """
        performs cleanup after the MainMenu is closed
        """
        print("cleaning up menu state")
    
    def startup(self) -> None:
        """ 
        Performs initialisation for the MainMenu
        """
        print('starting up menu state')
        
    def get_event(self, event) -> None:
        """
        Event listener
        """
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                print('escape pressed')
            if event.key == K_RETURN:
                self.done = True

    def update(self, screen) -> None:
        """
        Menu Logic
        """
        self.draw(screen)
    
    def draw(self, screen) -> None:
        """
        Graphics
        """

        screen.fill((25, 25, 112))

        title_font = pygame.font.SysFont("Verdana", size=32)
        small_font = pygame.font.SysFont("Verdana", size=20)

        title_box = pygame.Surface((400, 200))
        title_text = title_font.render(
            "Untitled bullet hell game", True, (255, 255, 255), (0, 0, 0)
        )
        title_rect = title_text.get_rect(center=(200, 100))

        start_box = pygame.Surface((200, 100))
        start_text = small_font.render("Start", True, (255, 255, 255), (0, 0, 0))
        start_rect = start_text.get_rect(center=(100, 50))

        title_box.blit(title_text, title_rect)
        screen.blit(title_box, (440, 100))
        start_box.blit(start_text, start_rect)
        screen.blit(start_box, (540, 400))

class Game(States):
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
    Pauses the game while in a level 
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    state_dict = {
        'main_menu': MainMenu(),
        'game': Game()
    }

    # set up the initial game state 
    current_state = state_dict['main_menu'] 
    current_state.startup()

    while current_state.quit == False:

        if current_state.done == True:
            previous, new_state_name = current_state.name, current_state.next
            current_state.cleanup()
            current_state = state_dict[new_state_name]
            current_state.done = False
            current_state.startup()
            current_state.previous = str(previous)
        
        while current_state.done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    current_state.quit = True
                    current_state.done = True

            current_state.get_event(event)
            
            clock.tick(current_state.fps)
            current_state.update(screen)
            pygame.display.update()


    # Cleanup the final game state if needed
    current_state.cleanup()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
