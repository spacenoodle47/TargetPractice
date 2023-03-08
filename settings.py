

class Settings:
    '''All settings for the game'''

    def __init__(self):
        '''Initialize the game settings'''

        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        #self.fps = 60

        # Rectangle
        self.rectangle_width = 20
        # Purple: (129, 55, 241) ???
        self.rectangle_color = (129, 55, 241)

        # Ship
        self.ship_speed = 1.5
        self.dynamic_stats()

        # Bullet
        self.bullet_speed = 6.0
        self.bullet_width = 50
        self.bullet_height = 30
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 3

        # Game
        self.game_active = True

        # Play button
        self.btn_play_width, self.btn_play_height = (50, 35)
        self.btn_color = (30, 30, 30)

        # Modifiers
        self.points_mod = 1.5
        self.speed_mod = 1.4
        self.height_mod = 1.3


    def dynamic_stats(self):
        '''Dynamic stats that reset/change on new game/during game'''
        self.ship_lives = 4
        self.game_points = 50
        self.rectangle_speed = 0.3
        self.rectangle_height = 100

    def increase_level(self):
        '''Increase difficulty of game'''
        self.game_points *= self.points_mod
        self.rectangle_speed *= self.speed_mod
        self.rectangle_height *= self.height_mod
