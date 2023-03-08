import pygame.font


class Button:
    '''Creates buttons for the game. Renders text image'''

    def __init__(self, tp, text):


        self.screen = tp.screen
        self.settings = tp.settings
        self.screen_rect = self.screen.get_rect()

        self.text_color = (230, 230, 0)

        # Create a font
        # TODO: use a different font
        self.font = pygame.font.SysFont(None, 48)



        self._render_play_btn(text)


    def _render_play_btn(self, text):
        '''Renders the text into a button image'''

        # Render
        self.play_image = self.font.render(text, False,
                   self.text_color, self.settings.btn_color).convert_alpha()

        # Create rect and set its starting pos
        self.play_rect = pygame.Rect(0, 0, self.settings.btn_play_width,
                                     self.settings.btn_play_height)

        # TODO: method/init arg for choosing button pos
        self.play_rect.center = self.screen_rect.center

        # Get rect & set position (inside button?)
        self.play_btn_rect = self.play_image.get_rect(
            center = self.play_rect.center)
        #self.btn_rect.center = self.rect.center


    def draw_button(self):
        '''Draws the button to the display surface'''
        self.screen.fill(self.settings.btn_color, self.play_rect)
        self.screen.blit(self.play_image, self.play_btn_rect)

