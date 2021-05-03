import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to manage an alien."""

    def __init__(self, game):
        """Initialize an alien."""
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen

        # Load the image and get its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """"""
