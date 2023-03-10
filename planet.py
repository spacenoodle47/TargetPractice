import pygame
from random import randint
from pygame.sprite import Sprite


class Planet(Sprite):
    '''Creates moving planets'''

    def __init__(self, tp, planet):
        super().__init__()
        self.screen = tp.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = tp.settings

        if planet == 'planet1':
            self.image = pygame.image.load('images/Planets/planet_1.png')
            self.rect = self.image.get_rect(
                topright = (self.screen_rect.right, randint(400, 800)))
        else:
            self.image = pygame.image.load('images/Planets/planet_5.png')
            self.rect = self.image.get_rect(
                bottomright = (self.screen_rect.right, randint(0, 400)))

        # finer adjustments
        self.x = self.rect.x

    def update(self):
        '''Updates the position of the planets'''
        self.x -= 0.5
        if self.rect.x <= -50:
            self.destroy()

        self.rect.x = self.x

    def destroy(self):
        '''Kills the planet ojects
        WHY CAN I CALL THIS METHOD OUTSIDE THIS CLASS?'''
        self.kill()