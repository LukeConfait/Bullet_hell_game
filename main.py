import pygame
from entities.Bullet import Bullet
from entities.Player import Player
import config

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
)


def paused():
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = False
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
        clock.tick(15)


def main():
    pygame.init
    global clock

    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    ADDBULLET = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDBULLET, 40)

    player = Player()
    # sprite groups
    bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    paused()
            if event.type == pygame.QUIT:
                running = False

            if event.type == ADDBULLET:
                new_bullet = Bullet()
                bullets.add(new_bullet)
                all_sprites.add(new_bullet)

        # logic

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        bullets.update()

        if pygame.sprite.spritecollideany(player, bullets):
            player.kill()
            running = False

        # graphics
        screen.fill((0, 0, 0))
        play_area = pygame.Surface((config.GAME_WIDTH, config.GAME_HEIGHT))
        play_area.fill((255, 255, 255))
        screen.blit(play_area, (30, 30))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
