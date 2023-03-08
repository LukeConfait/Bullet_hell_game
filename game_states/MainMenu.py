import pygame

from pygame.locals import (
    K_RETURN,
    K_UP,
    K_DOWN
)

from game_states.state import State

class MainMenu(State):
    """
    Main Menu Class
    """
    def __init__(self):
        super().__init__()
        self.name = 'main_menu'
    
    def cleanup(self) -> None:
        """
        performs cleanup after the MainMenu is closed
        """
        print("cleaning up menu state")
    
    def startup(self) -> None:
        """ 
        Performs initialisation for the MainMenu
        """
        self.buttons_index = 0 
        print('starting up menu state')

        self.title_font = pygame.font.SysFont("Verdana", size=32)
        self.small_font = pygame.font.SysFont("Verdana", size=20)

        self.inactive_text_color = (255, 255, 255)
        self.active_text_color = (255, 0, 0)
        
    def get_event(self) -> None:
        """
        Event listener
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
                self.done = True
            if event.type == pygame.KEYDOWN:

                if event.key == K_DOWN and self.buttons_index < 2:
                    self.buttons_index += 1
                    pygame.time.wait(150)
                elif event.key == K_UP and self.buttons_index > 0:
                    self.buttons_index -= 1
                    pygame.time.wait(150)

                if event.key == K_RETURN:
                    if self.buttons_index == 0:
                        self.next = 'game'
                        self.done = True
                    if self.buttons_index == 1:
                        self.next = 'high_scores'
                        self.done = True
                    if self.buttons_index == 2:
                        self.done = True
                        self.quit = True


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
        # Title box
        title_box = pygame.Surface((400, 200))
        title_text = self.title_font.render(
            "Untitled bullet hell game", True, (255, 255, 255), (0, 0, 0)
        )
        title_rect = title_text.get_rect(center=(200, 100))

        title_box.blit(title_text, title_rect)
        screen.blit(title_box, (440, 100))

        # Start box 
        start_box = pygame.Surface((200, 100))
        color = self.inactive_text_color
        if self.buttons_index == 0:
            color = self.active_text_color
        start_text = self.small_font.render("Start", True, color, (0, 0, 0))
        start_rect = start_text.get_rect(center=(100, 50))
        start_box.blit(start_text, start_rect)
        screen.blit(start_box, (540, 400))

        # High score box
        high_score_box = pygame.Surface((200,100))
        color = self.inactive_text_color
        if self.buttons_index == 1:
            color = self.active_text_color
        high_score_text = self.small_font.render("High Scores", True, color, (0,0,0))
        high_score_rect = high_score_text.get_rect(center=(100,50))
        high_score_box.blit(high_score_text,high_score_rect)
        screen.blit(high_score_box, (540, 600))

        # Quit box 
        quit_box = pygame.Surface((200,100))
        color = self.inactive_text_color
        if self.buttons_index == 2:
            color = self.active_text_color
        quit_text = self.small_font.render("Quit", True, color, (0, 0, 0))
        quit_rect = quit_text.get_rect(center=(100,50))
        quit_box.blit(quit_text,quit_rect)
        screen.blit(quit_box, (540, 800))
