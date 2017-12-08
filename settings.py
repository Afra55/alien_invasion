class Settings:

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        self.alien_speed_factor = 1  # 水平移动速度
        self.fleet_drop_speed = 10  # 垂直移动速度
        self.fleet_direction = 1  # 1 向右移动， -1 向左移动
