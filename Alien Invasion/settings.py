class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 40, 80)
        self.full_screen_mode = True  # NOT IMPLEMENTED / True by default
        # Настройки корабля
        self.ship_speed = 0.6
        self.boost_multiplier = 2