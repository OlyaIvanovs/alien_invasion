class GameState:
    """Statistics for Alien Invasion."""

    def __init__(self, game):
        """Initialize the statistics."""
        self.settings = game.settings
        self.game_active = False
        self.score = 0
        self.reset_stat()

        # High score should never be reset
        self.high_score = 0

    def reset_stat(self):
        """Initialize the statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
