import pygame

from pygame.locals import (
    K_ESCAPE
)

from game_states.state import State

class HighScores(State):
    
    def __init__(self):
        super().__init__()
        self.next = 'main_menu'
        self.name = 'high_scores'

    def cleanup(self) -> None:
        """
        Cleans up the state
        """    
    def startup(self) -> None:
        """
        Initialises the state
        """
        self.title_font = pygame.font.SysFont("Verdana", size=32)

    def get_event(self, event) -> None:
        """
        Event listener
        """
        if event.type == pygame.KEYDOWN:
            
            if event.key == K_ESCAPE:
                self.done = True
            

    def update(self, screen) -> None:
        """
        Non event loop logic
        """
        self.draw(screen)

    def draw(self, screen) -> None:
        """
        Graphics
        """
        screen.fill((25, 25, 112))

        title_box = pygame.Surface((400, 100))
        title_text = self.title_font.render(
            "High Scores", True, (255, 255, 255), (0, 0, 0)
        )
        title_rect = title_text.get_rect(center=(200, 50))

        title_box.blit(title_text, title_rect)
        screen.blit(title_box, (440, 100))
