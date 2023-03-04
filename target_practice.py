import sys
from time import sleep
import pygame

from settings import Settings
from rectangle import Rectangle
from rocket_launcher import RocketLauncher
from bullet import Bullet
from button import Button


class TargetPractice:
    '''Main game object'''

    def __init__(self):
        '''Initialize objects and attributes for the main game'''

        # INITIALIZE PYGAME... EVERYTHING WORKS BUT NEED FOR FONT???????
        pygame.init()

        # Settings object
        self.settings = Settings()

        # Create surface
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        # Clock object for the framerate
        #self.clock = pygame.time.Clock()

        self.rocket_launcher = RocketLauncher(self)

        # Create instance of Rectangle class
        self.rectangle = Rectangle(self)
        self.btn_play = Button(self)

        # Create a group for the bullets
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        '''The main loop of the game'''

        while True:

            self._check_events()

            if self.settings.game_active:

                self.rocket_launcher.move()
                self._update_bullets()
                self.rectangle.moving_vertically()

            self._update_screen()


    def _check_events(self):
        '''Check for events that are triggered in the game'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_press(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_release(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                self._new_game(mouse_pos)


    def _check_keydown_press(self, event):
        '''Responds to keydown presses'''
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.rocket_launcher.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket_launcher.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_release(self, event):
        '''Respond to keyup release'''
        if event.key == pygame.K_UP:
            self.rocket_launcher.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket_launcher.moving_down = False

    def _fire_bullets(self):
        '''Creates instances of Bullet and adds it to the bullets group'''

        # Just +1 for tidyness in code -- probably useless in practice
        if (len(self.bullets) + 1) <= self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _new_game(self, mouse_pos):
        '''On Play-button click: start new game'''

        # If a given argument's point is overlapping
        # with the corresponding rect
        button_pressed = self.btn_play.btn_rect.collidepoint(mouse_pos)
        if button_pressed and not self.settings.game_active:
            self.settings.game_active = True
            self.rocket_launcher.center_rocket()
            self.settings.dynamic_stats()
            self.bullets.empty()
            pygame.mouse.set_visible(False)



    def _game_over(self):
        '''When the ships loses its lifes'''
        self.settings.ship_lives -= 1
        if self.settings.ship_lives == 0:
            self.settings.game_active = False

    def _update_bullets(self):
        '''Handles the creation, removal and collision of bullets.
        Also updates its position'''

        collision = pygame.sprite.spritecollide(self.rectangle, self.bullets, True)

        self.bullets.update()
        # Iterate over copy of the group to remove items while iterating
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
                self._game_over()

    def _update_screen(self):
        '''Draws the objects to the screen and redraws the screen'''

        # Set background color of the surface
        self.screen.fill(self.settings.bg_color)

        # Draw Rectangle to the screen
        self.rectangle.drawme()

        # Draw rocket launcher to the screen
        self.rocket_launcher.blitme()

        # Draw the bullets to the display surface
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # If the game is inactive
        if not self.settings.game_active:
            self.btn_play.draw_button()
            pygame.mouse.set_visible(True)

        # Redraw the screen at the end of the method
        pygame.display.update()
        #pygame.display.flip()

        # Set the max frame rate of the game
        #self.clock.tick(self.settings.fps)

if __name__ == '__main__':
    tp = TargetPractice()
    tp.run_game()