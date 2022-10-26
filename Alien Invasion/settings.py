class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 20, 30)
        # Настройки корабля
        self.ship_speed = 1
        self.boost_multiplier = 2
        self.ship_limit = 1
        # Настройки снарядов
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullet_limit = 5
        # Настройки пришельцев
        self.alien_speed = 5
        self.fleet_drop_speed = 100
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1