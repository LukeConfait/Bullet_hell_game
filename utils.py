import pygame
import json
import os

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
)

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

def save_score(score: int, name: str = 'AAA'):
    """
    Saves scores to a json object, if no file exists it creates the file
    """

    path = 'scores/scores.json'

    if os.path.exists(path):
        with open(path, 'r') as file:
            scores = json.load(file)
            scores.append([name, score])
        with open(path, 'w') as file:
            file.write(json.dumps(scores, indent=4))
    else:
        with open(path, 'x') as file:
            file.write(json.dumps([[name, score]], indent=4))

def draw_text_to_box(screen, box_size, box_color, text, font, text_color, blit_dest, **kwargs) -> None:
    """
    Custom function for drawing text to a text box
    """
    box = pygame.Surface(box_size)
    box.fill(box_color)
    text_to_render = font.render(text, True, text_color)
    text_rect = text_to_render.get_rect(**kwargs)

    box.blit(text_to_render, text_rect)
    screen.blit(box, blit_dest)