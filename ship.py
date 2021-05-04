import pygame


class Ship:
    """A class to manage a ship"""

    def __init__(self, game):
        """Initialize the ship and set its first position."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        # Load the image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.moving_right = False
        self.moving_left = False

        self.center_ship()

    def center_ship(self):
        """"""
        # Start each new ship at the center of the screen's bottom
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ships position."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
