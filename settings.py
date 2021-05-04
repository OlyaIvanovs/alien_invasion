class Settings:
    """A class to store all settings for Allien Invasion."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Game settings
        self.ship_limit = 3
