import pygame
from settings import Settings
from pygame.sprite import Sprite

class Rectangle(Sprite):
    '''Rectangle object: Will be used as the "enemy" target practice.'''

    # Inherit from super class
    def __init__(self, tp):

        super().__init__()

        self.screen = tp.screen
        self.settings = tp.settings
        self.screen_rect = self.screen.get_rect()

        # Make a Rect from scratch
        self.rect = pygame.Rect(0, 0, self.settings.rectangle_width,
                                self.settings.rectangle_height)

        # Set starting position
        # -- middle right side
        self.rect.right = self.screen_rect.right - 40
        self.rect.top = self.settings.screen_height / 2

        # Attribute for finer movement (float)
        self.y = float(self.rect.y)

        # Movement flag???

        # direction of the rectangle
        # -- 1 is up, -1 is down
        self.rectangle_direction = 1

    # TODO: fix this?
    def center_rectangle(self):
        '''Center rectangle on init and when game restarts'''
        self.rect.right = self.screen_rect.right - 40
        self.rect.top = self.settings.screen_height / 2

        self.y

    # -- Method for updating position
    def moving_vertically(self):
        '''Updates position of the rectangle.
        Moves up at the start of the game.'''

        # When the rectangle hits the top or the bottom of the screen,
        # the direction of the rectangle will change
        if (self.rect.top <= 0 or
                (self.rect.bottom >= self.settings.screen_height)):
            self.rectangle_direction *= -1

        self.y -= self.settings.rectangle_speed * self.rectangle_direction
        self.rect.y = self.y

    # -- Method for drawing to screen
    def drawme(self):
        '''Draws the rectangle to the screen'''
        pygame.draw.rect(self.screen,
             self.settings.rectangle_color, self.rect)

        # Can I use spriteGroup built-in .draw() method instead??