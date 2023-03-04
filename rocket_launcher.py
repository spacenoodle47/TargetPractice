import pygame

class RocketLauncher:
    '''Attributes of the RocketLauncher,
    which will be controlled by the player'''

    def __init__(self, tp):
        '''Initialize attributes for the Rocket Launcher class'''

        self.screen = tp.screen
        self.settings = tp.settings
        self.screen_rect = self.screen.get_rect()

        # get image & get its rect
        self.image = pygame.image.load("images/rocket_launcher.bmp")

        # Get image height & width to resize the image
        self.width, self.height = self.image.get_rect().size
        self.image_resized = pygame.transform.scale(self.image,
                            (self.width * 0.5, self.height * 0.5))
        # Invert the picture
        self.image_flip = pygame.transform.flip(
                self.image_resized, True, False)
        #self.rect = self.image.get_rect()
        self.rect = self.image_flip.get_rect()

        # Set staring position
        # self.rect.midleft = self.screen_rect.midleft
        # self.rect.left = self.screen_rect.left
        self.center_rocket()

        # Float attribute for more precise vertical movement
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False


    def move(self):
        '''Takes care of moving the rocket launcher vertically'''

        if self.moving_up and self.rect.top >= 0:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def center_rocket(self):
        '''Recenters the rocket when restarting the game'''
        self.rect.midleft = self.screen_rect.midleft
        self.rect.left = self.screen_rect.left

        self.y = self.rect.y

    # -- Method for drawing to screen
    def blitme(self):
        '''Draw the rocket launcher to the screen'''
        self.screen.blit(self.image_flip, self.rect)