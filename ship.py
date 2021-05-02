import pygame


class Ship:
    """A class to manage a ship"""

    def __init__(self, game):
        """Initialize the ship and set its first position."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the center of the screen's bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship"""
        self.screen.blit(self.image, self.rect)
