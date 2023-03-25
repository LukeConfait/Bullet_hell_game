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

def save_score(score: int, name: str):
    """
    Saves scores to a json object, if no file exists it creates the file
    """

    # This breaks if there is an empty scores.json file

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

