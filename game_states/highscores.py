import json
import pygame

from pygame.locals import (
    K_ESCAPE
)


from operator import itemgetter

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
    def startup(self, screen) -> None:
        """
        Initialises the state
        """
        # Graphics startup
        self.title_font = pygame.font.SysFont("Verdana", size=40)
        self.small_font = pygame.font.SysFont("Verdana", size=24)
        
        screen.fill((25, 25, 112))

        title_block = pygame.Surface((400, 100))
        title_block.fill((0, 0, 0))
        title_text = self.title_font.render("High Scores", True, (255, 255, 255))
        title_text_rect = title_text.get_rect(center=(200, 50))
        title_block.blit(title_text,title_text_rect)
        screen.blit(title_block, (440, 100))

        self.full_block = pygame.Surface((880, 50))
        self.full_block.fill((50, 50, 112))
        
        self.number_block = pygame.Surface((50, 50))
        self.number_block.fill((0, 0, 0))

        self.name_block = pygame.Surface((400, 50))
        self.name_block.fill((0, 0, 0))
        
        self.score_block = pygame.Surface((400, 50))
        self.score_block.fill((0, 0, 0))

        # Load score file
        with open("scores/scores.json", 'r') as file:
            self.scores = json.load(file)

            while len(self.scores) < 10:
                self.scores.append(["---", 0])

            self.scores = sorted(self.scores, key=lambda x : x[1], reverse=True)

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


        for i in range(10):

            number_block = self.number_block.copy()
            number_text = self.small_font.render(f"{i + 1}", True, (255, 255, 255))
            number_rect = number_text.get_rect(center=(25, 25))
            number_block.blit(number_text, number_rect)

            name_block = self.score_block.copy()
            name_text  = self.small_font.render(self.scores[i][0], True, (255, 255, 255))
            name_rect = name_text.get_rect(left=0, centery=25)
            name_block.blit(name_text, name_rect)

            score_block = self.score_block.copy()
            score_text = self.small_font.render(f"{self.scores[i][1]}", True, (255, 255, 255))
            score_rect = score_text.get_rect(right=400, centery=25)
            score_block.blit(score_text, score_rect)

            block = self.full_block

            block.blit(number_block, (0, 0))
            block.blit(name_block, (65, 0))
            block.blit(score_block, (480, 0))

            screen.blit(block, (200, 300 + 60 * i))
            



