import pygame

class Rocket():
    """Класс для управления кораблем."""

    def __init__(self, r_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = r_game.screen
        self.settings = r_game.settings
        self.screen_rect = r_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('./img/rocket.png')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется в центре экрана.
        self.rect.center = self.screen_rect.center
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # Сохранение координат центра корабля
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Флаг ускорения скорости корабля
        self.speed_boost = False

    def update(self):
        """Обновляет позицию корабля с учетом флагов."""
        new_rocket_speed = 0
        if self.speed_boost: 
            new_rocket_speed = self.settings.rocket_speed * self.settings.boost_multiplier
        else:
            new_rocket_speed = self.settings.rocket_speed
        self._update_x(new_rocket_speed)
        self._update_y(new_rocket_speed)



    def _update_x(self,new_rocket_speed):
        """Обновляет позицию корабля по оси x"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += new_rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= new_rocket_speed
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def _update_y(self,new_rocket_speed):
        """Обновляет позицию корабля по оси y"""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += new_rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= new_rocket_speed
        # Обновление атрибута rect на основании self.y
        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)