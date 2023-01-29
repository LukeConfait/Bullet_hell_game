import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_LSHIFT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((5, 5))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                (SCREEN_WIDTH - self.surf.get_width()) / 2,
                (SCREEN_HEIGHT - self.surf.get_height()) / 2,
            )
        )

    def update(self, pressed_keys):
        speed = 6
        if pressed_keys[K_LSHIFT]:
            speed = 2
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, speed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(speed, 0)

        if self.rect.left < 30:
            self.rect.left = 30
        if self.rect.right > 30 + GAME_WIDTH:
            self.rect.right = 30 + GAME_WIDTH
        if self.rect.top <= 30:
            self.rect.top = 30
        if self.rect.bottom >= SCREEN_HEIGHT - 30:
            self.rect.bottom = SCREEN_HEIGHT - 30


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((64, 224, 208))
        self.rect = self.surf.get_rect(top=30, left=random.randint(30, GAME_WIDTH + 20))
        self.speed = 4
        self.kill_next_frame = False
        self.just_created = True

    def update(self):
        if self.just_created == False:
            if self.kill_next_frame == True:
                self.kill()
            if self.rect.bottom + self.speed > SCREEN_HEIGHT - 30:
                self.rect.move_ip(0, (SCREEN_HEIGHT - self.rect.bottom) - 30)
                self.kill_next_frame = True
                return
            self.rect.move_ip(0, self.speed)
            return
        self.just_created = False


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
    global SCREEN_HEIGHT, SCREEN_WIDTH, clock, GAME_HEIGHT, GAME_WIDTH
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 960

    GAME_WIDTH = 800
    GAME_HEIGHT = 900

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
        play_area = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        play_area.fill((255, 255, 255))
        screen.blit(play_area, (30, 30))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
