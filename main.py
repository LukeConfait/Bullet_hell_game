import pygame
import sys

from game_states.mainmenu import MainMenu
from game_states.game import Game
from game_states.highscores import HighScores

import config

def main():
    # Inititalise pygame 
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create a state dictionary to store the game states needed for the game
    state_dict = {
        'main_menu': MainMenu(),
        'game': Game(),
        'high_scores': HighScores(),
    }

    # set up the initial game state 
    current_state = state_dict['main_menu'] 
    current_state.startup(screen)

    while current_state.quit == False:

        # change to the next state if the current state is finished
        if current_state.done == True:
            previous, new_state_name = current_state.name, current_state.next
            current_state.cleanup()
            current_state = state_dict[new_state_name]
            current_state.done = False
            current_state.startup(screen)
            current_state.previous = str(previous)
        
        while current_state.done == False:
            
            # Run the event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    current_state.quit = True
                    current_state.done = True
                current_state.get_event(event)
            # Update the current state outside of the event loop
            current_state.update(screen)

            font = pygame.font.SysFont("Verdana", size=20)
            fps_display = pygame.Surface((100,100))
            fps = round(clock.get_fps(), 2)
            fps_text = font.render(str(fps) + 'fps', True, (255, 255, 255))
            fps_rect = fps_text.get_rect(center=(50,50))
            fps_display.blit(fps_text, fps_rect)
            screen.blit(fps_display, (config.SCREEN_WIDTH-100, config.SCREEN_HEIGHT-100))

            clock.tick(current_state.fps)
            pygame.display.update()

    # Cleanup the final game state if needed
    current_state.cleanup()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
