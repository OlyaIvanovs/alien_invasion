import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game):
        """Create a bullet in the current ship position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.color = self.settings.bullet_color
        self.rect.midtop = game.ship.rect.midtop

        # Store a bullet's position as s decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rest position.
        self.rect.y = self.y

    def draw(self):
        """Draw the bullet."""
        pygame.draw.rect(self.screen, self.color, self.rect)
