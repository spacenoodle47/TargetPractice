import pygame.font


class Button:
    '''Creates buttons for the game. Renders text image'''

    def __init__(self, tp):


        self.screen = tp.screen
        self.settings = tp.settings
        self.screen_rect = self.screen.get_rect()

        self.text_color = (230, 230, 0)

        # Create a font
        self.font = pygame.font.SysFont(None, 48)

        # Create rect and set its starting pos
        self.rect = pygame.Rect(0, 0, self.settings.btn_play_width,
                                self.settings.btn_play_height)
        self.rect.center = self.screen_rect.center

        self._render_play_btn()


    def _render_play_btn(self):
        '''Renders the text into a button image'''

        text = 'Play'
        # Render
        self.text_image = self.font.render(text, False,
                                           self.text_color, self.settings.btn_color)

        # Get rect & set position (inside button?)
        self.btn_rect = self.text_image.get_rect()
        self.btn_rect.center = self.rect.center

    def draw_button(self):
        '''Draws the button to the display surface'''
        self.screen.fill(self.settings.btn_color, self.rect)
        self.screen.blit(self.text_image, self.btn_rect)

