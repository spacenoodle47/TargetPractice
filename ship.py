import pygame

class Ship:
    '''Attributes of the Ship,
    which will be controlled by the player'''

    def __init__(self, tp):
        '''Initialize attributes for the Ship class'''

        self.screen = tp.screen
        self.settings = tp.settings
        self.screen_rect = self.screen.get_rect()

        # get image & get its rect
        self.image = pygame.image.load("images/Ships/ship_4.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        self._init_health()

        # Set staring position
        # self.rect.midleft = self.screen_rect.midleft
        # self.rect.left = self.screen_rect.left
        self.center_ship()

        # Float attribute for more precise vertical movement
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False


    def move(self):
        '''Takes care of moving the ship vertically'''

        if self.moving_up and self.rect.top >= 0:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def center_ship(self):
        '''Recenters the ship when restarting the game'''
        self.rect.midleft = self.screen_rect.midleft
        self.rect.left = self.screen_rect.left

        self.y = self.rect.y

    def _init_health(self):
        '''Initialize the health surfaces'''
        hp1 = pygame.image.load('images/Health/hp_1.png').convert_alpha()
        hp1_width, hp1_height = hp1.get_rect().size
        hp1 = pygame.transform.scale(hp1, (hp1_width * 0.5, hp1_height * 0.5))
        hp2 = pygame.image.load('images/Health/hp_2.png').convert_alpha()
        hp2_width, hp2_height = hp2.get_rect().size
        hp2 = pygame.transform.scale(hp2, (hp2_width * 0.5, hp2_height * 0.5))
        hp3 = pygame.image.load('images/Health/hp_3.png').convert_alpha()
        hp3_width, hp3_height = hp3.get_rect().size
        hp3 = pygame.transform.scale(hp3, (hp3_width * 0.5, hp3_height * 0.5))
        hp4 = pygame.image.load('images/Health/hp_4.png').convert_alpha()
        hp4_width, hp4_height = hp4.get_rect().size
        hp4 = pygame.transform.scale(hp4, (hp4_width * 0.5, hp4_height * 0.5))
        self.health_index = 0
        # TODO: fix index out of range
        self.health = [hp4, hp3, hp2, hp1]
        self.health_rect = self.health[self.health_index].get_rect(
            topleft = self.screen_rect.topleft)

    def lose_health(self):
        '''Lose health +
        Fixes the issue with health index out of range of the list'''
        if self.health_index == 3:
            self.health_index = 0

        self.health_index += 1

    def show_health(self):
        '''Draws the health surface onto display surface'''
        self.screen.blit(self.health[self.health_index], self.health_rect)

    # -- Method for drawing to screen
    def blitme(self):
        '''Draw the ship to the screen'''
        self.screen.blit(self.image, self.rect)

        # Is it better to make everything a Sprite???