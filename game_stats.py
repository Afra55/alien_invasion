class GameStatus:

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.ships_left = self.ai_settings.ship_limit
        self.game_active = True

    def reset_status(self):
        self.ships_left = self.ai_settings.ship_limit
