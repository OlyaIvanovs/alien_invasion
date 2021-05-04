class GameState:
    """Statistics for Alien Invasion."""

    def __init__(self, game):
        """Initialize the statistics."""
        self.settings = game.settings
        self.game_active = True
        self.reset_stat()

    def reset_stat(self):
        """Initialize the statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
