import pygame

from pygame.locals import (
    K_ESCAPE,
    K_RETURN,
    K_BACKSPACE,
)

from entities.player import Player
from entities.bullet import Bullet

from game_states.state import State

import config
import utils


class Game(State):
    """
    Game Class
    """

    def __init__(self):
        super().__init__()
        self.next = "main_menu"
        self.name = "game"
        self.fps = 60

    def cleanup(self) -> None:
        """
        Cleans up the game state
        """
        print("Cleaning up game state")

    def startup(self, screen) -> None:
        """
        Initialises the game state
        """
        print("starting up game state")
        # set up fonts
        self.font = pygame.font.SysFont("Verdana", size=40)
        self.small_font = pygame.font.SysFont("Verdana", size=32)
        # set up play area
        self.play_area = pygame.Surface((config.GAME_WIDTH, config.GAME_HEIGHT))
        self.play_area.fill((255, 255, 255))
        # create player and sprite groups
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        # create user event for adding bullets and bullet sprite group
        self.ADDBULLET = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDBULLET, 40)
        self.bullets = pygame.sprite.Group()
        # setup game score
        self.score = 0
        self.name = ""

        # Logic conditions
        self.enter = False
        self.game_over = False

        # Initial graphics
        screen.fill((0, 0, 0))

        score_title = pygame.Surface((390, 100))
        score_title.fill((255, 255, 255))
        score_title_text = self.font.render("Score", True, (0, 0, 0))
        score_title_rect = score_title_text.get_rect(center=(195, 50))

        score_title.blit(score_title_text, score_title_rect)
        screen.blit(score_title, (860, 30))

        self.score_board = pygame.Surface((390, 100))

    def get_event(self, event) -> None:
        """
        Event listener
        """

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                utils.paused()

        if self.game_over == False:
            if event.type == self.ADDBULLET:
                new_bullet = Bullet()
                self.bullets.add(new_bullet)
                self.all_sprites.add(new_bullet)

        elif event.type == pygame.KEYDOWN:
            if event.key == K_RETURN:
                self.enter = True
            elif event.key == K_BACKSPACE:
                self.name = self.name[:-1]
            else:
                self.name += event.unicode

    def update(self, screen) -> None:
        """
        Non event loop game logic
        """
        pressed_keys = pygame.key.get_pressed()
        self.player.update(pressed_keys)
        if self.game_over == False:

            self.bullets.update()

            # This feels kinda bad but im unsure how to implement it into the bullet update
            for bullet in self.bullets:
                if bullet.kill_next_frame == True:
                    self.score += 15

            if pygame.sprite.spritecollideany(self.player, self.bullets):
                self.game_over = True

        else:
            if self.enter == True:
                score = self.score
                utils.save_score(score, self.name)
                self.done = True

        self.draw(screen)

    def draw(self, screen) -> None:
        """
        Graphics
        """
        screen.blit(self.play_area, (30, 30))

        score_text = self.font.render(f"{self.score}", True, (0, 0, 0))
        score_rect = score_text.get_rect(right=390, centery=50)

        self.score_board.fill((255, 255, 255))
        self.score_board.blit(score_text, score_rect)
        screen.blit(self.score_board, (860, 140))

        for entity in self.all_sprites:
            screen.blit(entity.surf, entity.rect)

        if self.game_over == True:
            game_over_block = pygame.Surface((400, 100))

            # game_over_text = self.font.render(f"Haha you suck",True,(0,0,0))
            game_over_text = self.font.render(f"GAME OVER", True, (255, 255, 255))
            game_over_rect = game_over_text.get_rect(center=(200, 50))
            game_over_block.blit(game_over_text, game_over_rect)
            screen.blit(game_over_block, (230, 130))

            # Title for the name input box
            name_input_title_block = pygame.Surface((300, 100))
            name_input_title_text = self.small_font.render(
                "Input your name:", True, (255, 255, 255)
            )
            name_input_title_rect = name_input_title_text.get_rect(center=(150, 50))
            name_input_title_block.blit(name_input_title_text, name_input_title_rect)
            screen.blit(name_input_title_block, (280, 330))

            # Interactive box for displaying the name

            name_input_block = pygame.Surface((300, 100))
            name_input_text = self.small_font.render(
                f"{self.name}", True, (255, 255, 255)
            )
            name_input_rect = name_input_text.get_rect(left=(10), centery=(50))
            name_input_block.blit(name_input_text, name_input_rect)
            screen.blit(name_input_block, (280, 530))
