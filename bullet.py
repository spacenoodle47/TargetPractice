import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Class that takes care of the bullets shot from the rocket launcher'''

    def __init__(self, tp):

        super().__init__()

        self.screen = tp.screen
        self.screen_rect = self.screen.get_rect()
        self.ship = tp.rocket_launcher
        self.settings = tp.settings

        # Create rect and set position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midleft = self.ship.rect.midright

        # Finer adjustment
        self.x = float(self.rect.x)


    def update(self):
        '''Update the position of the bullet'''
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        '''Draws the bullet to the screen'''
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)

