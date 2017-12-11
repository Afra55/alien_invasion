class Settings:

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        self.fleet_direction = 1  # 外星人移动方向 1 向右移动， -1 向左移动

        self.speedup_scale = 1.1  # 游戏节奏
        self.score_scale = 1.5  # 击杀外星人得分提高速度

        self.initialize_dynamic_settings()

    # noinspection PyAttributeOutsideInit
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5  # 飞船移动速度
        self.bullet_speed_factor = 3  # 子弹移动速度
        self.alien_speed_factor = 1  # 外星人水平移动速度
        self.fleet_drop_speed = 10  # 外星人垂直移动速度

        self.alien_points = 50  # 每击杀一个外星人的得分

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        # noinspection PyAttributeOutsideInit
        self.alien_points = int(self.alien_points * self.score_scale)
