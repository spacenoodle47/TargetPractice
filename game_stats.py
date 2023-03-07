import pygame

class GameStats:
    '''Takes care of all the stats related to the game'''

    def __init__(self, tp):

        self.screen = tp.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = tp.settings

        # Font object
        self.font = pygame.font.SysFont(None, 48)

        # Random color
        self.score_color = (149, 32, 87)
        self.score = 0

        self.render_score()

        # -- Render method
    def render_score(self):
        '''Renders the score image and set its position'''
        self.text = str(self.score)
        self.score_image = self.font.render(self.text, False, self.score_color).convert_alpha()
        self.score_rect = self.score_image.get_rect(
            centerx = self.screen_rect.centerx,
            centery = self.screen_rect.top + 50)

        # -- Draw method
    def draw(self):
        '''Draws the gamestats to the screen'''
        self.screen.blit(self.score_image, self.score_rect)