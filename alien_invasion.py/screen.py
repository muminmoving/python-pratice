import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet


class Alien_invasion:
    def __init__(self):
        # 初始化游戏
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings = Settings()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)
        self.bullet = Bullet(self)
        self.bullets = pygame.sprite.Group()


        pygame.display.set_caption("Alien_invasion")

    def run_game(self):
        while True:
            self._apdate_screen()
            # 飞船移动
            self.ship.update()
            self._check_events()
            self.bullet.update()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        new_bullet = self.bullet
        self.bullets.add(new_bullet)

    def _apdate_screen(self):
        # 显示屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            self.bullet.draw_bullet()
        pygame.display.flip()

if __name__ == "__main__":
    ai = Alien_invasion()
    ai.run_game()
