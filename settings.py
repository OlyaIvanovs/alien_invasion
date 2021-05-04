class Settings:
    """A class to store all settings for Allien Invasion."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 50

        # Game settings
        self.ship_limit = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the aliens score increase.
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize the settings that change throught the game."""
        self.ship_speed = 1.5
        self.alien_speed = 0.5
        self.bullet_speed = 2.0

        self.alien_score = 50

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien score."""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_score *= self.score_scale
