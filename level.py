class Level:
    def __init__(self, bomb, enemy):
        self.bomb = bomb
        self.enemy = enemy
        self.lose_grid = False
        self.win_grid = False
        self.game_beat_grid = False
        self.level_temp_delay = 0
        self.speed = 0.1
        self.player_pos_x = 0
        self.player_pos_y = 0

    def next(self, level):
        bomb_number = self.bomb.level_update(level)
        self.bomb.number_placed = bomb_number
        self.bomb.number_left = bomb_number

    def check_for_enemies(self, grid_size):
        if self.bomb.delay >= grid_size + 1:
            self.level_temp_delay += 0.1
            if self.level_temp_delay >= 15:
                if not self.enemy.positions:
                    self.win_grid = True
                else:
                    self.lose_grid = True

    def update_grid(self, grid_ui):
        if self.win_grid:
            if grid_ui.win_screen():
                return "Win"
        if self.lose_grid:
            if grid_ui.lose_screen():
                return "Lose"
        if self.game_beat_grid:
            if grid_ui.game_complete_screen():
                return "Finish"

    def create(self, enemy, grid_ui):
        grid_ui.game_end_delay = 0
        self.enemy = enemy
        self.enemy.placed = False
        self.bomb.explode_on = False
        self.lose_grid = False
        self.win_grid = False
        self.speed = 0.1
        self.bomb.delay = 0
        self.level_temp_delay = 0
        self.bomb.number_placed = 0
        self.bomb.number_left = 0
        self.player_pos_x = 0
        self.player_pos_y = 0
        self.bomb.positions = []
        self.enemy.positions = []
