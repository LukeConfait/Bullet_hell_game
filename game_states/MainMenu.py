import pygame

from pygame.locals import (
    K_ESCAPE,
    K_RETURN,
)

from game_states import State

class MainMenu(State):
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
