class Settings():
    """Класс для хранения всех настроек игры"""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (153, 204, 255)
        # Настройки корабля
        self.rocket_speed = 0.6
        self.boost_multiplier = 2