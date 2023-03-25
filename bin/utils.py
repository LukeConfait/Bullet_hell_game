import pygame
import json
import os

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
)


def paused() -> None:
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
    Saves score to json
    """
    path = "scores/scores.json"

    with open(path, "r") as file:
        scores = json.load(file)
        scores.append([name, score])
    with open(path, "w") as file:
        json.dump(scores, file, indent=4)
