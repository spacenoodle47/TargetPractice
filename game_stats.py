import pygame

class GameStats:
    '''Takes care of all the stats related to the game'''

    def __init__(self, tp):

        self.screen = tp.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = tp.settings

        # Font object
        self.font = pygame.font.SysFont(None, 48)

        # Scores
        self.score = 0
        self.high_score = 0
        self.score_color = (149, 32, 87)

        self.render_score()
        self.render_high_score()

        # -- Render method
    def render_score(self):
        '''Renders the score image and set its position'''
        text = str("{:,}".format(round(int(self.score)), -1))
        self.score_image = self.font.render(
            text, False, self.score_color).convert_alpha()
        self.score_rect = self.score_image.get_rect(
            centerx = self.screen_rect.centerx,
            centery = self.screen_rect.top + 50)

    def render_high_score(self):
        '''Renders the high score and set its position'''
        #TODO : change position with score on active/inactive

        if self.score > self.high_score:
            self.high_score = self.score

        text = "Highscore: " + str(int(self.high_score))
        self.high_score_image = self.font.render(
            text, False, self.score_color).convert_alpha()
        self.high_score_rect = self.high_score_image.get_rect(
            centerx = self.screen_rect.centerx,
            centery = self.screen_rect.top + 80)


        # -- Draw method
        # Create just one method
    def draw(self):
        '''Draws the gamestats to the screen'''
        self.screen.blit(self.score_image, self.score_rect)

    def draw_high(self):
        '''Draws the high score to the screen'''
        self.screen.blit(self.high_score_image, self.high_score_rect)