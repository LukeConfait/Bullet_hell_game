import pygame
import sys

from game_states.MainMenu import MainMenu
from game_states.Game import Game

import config

def main():
    # Inititalise pygame 
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create a state dictionary to store the game states needed for the game
    state_dict = {
        'main_menu': MainMenu(),
        'game': Game()
    }

    # set up the initial game state 
    current_state = state_dict['main_menu'] 
    current_state.startup()

    while current_state.quit == False:

        # change to the next state if the current state is finished
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
