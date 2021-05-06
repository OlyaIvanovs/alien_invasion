import pygame
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """Report score information."""

    def __init__(self, game):
        """"""
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = game.stats
        self.game = game

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial scoring information.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score text into the image."""
        rounded_score = round(self.stats.score, -1)
        score = "{:,}".format(rounded_score)
        self.score_img = self.font.render(
            score, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.top = 20
        self.score_img_rect.right = self.screen_rect.right - 20

    def prep_high_score(self):
        """Turn the high score into the image."""
        high_score_rounded = round(self.stats.high_score, -1)
        hight_score_str = "{:,}".format(high_score_rounded)
        self.high_score_img = self.font.render(
            hight_score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top top of the screen
        self.high_score_img_rect = self.high_score_img.get_rect()
        self.high_score_img_rect.centerx = self.screen_rect.centerx
        self.high_score_img_rect.top = 20

    def prep_level(self):
        """Turn the level into the image."""
        level_str = str(self.stats.level)
        self.level_img = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_img_rect = self.level_img.get_rect()
        self.level_img_rect.top = self.score_img_rect.bottom + 10
        self.level_img_rect.right = self.score_img_rect.right

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_img, self.score_img_rect)
        self.screen.blit(self.high_score_img, self.high_score_img_rect)
        self.screen.blit(self.level_img, self.level_img_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Check if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.prep_level()
