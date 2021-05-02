import sys
import pygame
import settings
import ship


class AllienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and create game resources."""
        pygame.init()

        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Allien Invasion")
        self.bg_color = self.settings.bg_color
        self.ship = ship.Ship(self)

    def _check_events(self):
        """Respond to keypress and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """"""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """Start main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    game = AllienInvasion()
    game.run_game()
