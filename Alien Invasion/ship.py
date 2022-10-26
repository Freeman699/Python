import pygame

class Ship:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля, изменяет размер и получает прямоугольник.
        scale_multiplier = 0.04
        scaled_img = pygame.transform.scale(
            pygame.image.load('./img/main_ship.png'),
                (self.settings.screen_width * scale_multiplier,
                self.settings.screen_height * (scale_multiplier * 2)
                )
            )
        self.image = scaled_img
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        # Сохранение координаты x центра корабля
        self.x = float(self.rect.x)
        # Флаг ускорения скорости корабля
        self.speed_boost = False

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Обновляет позицию корабля с учетом флагов."""
        new_ship_speed = 0
        if self.speed_boost: 
            new_ship_speed = self.settings.ship_speed * self.settings.boost_multiplier
        else:
            new_ship_speed = self.settings.ship_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += new_ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= new_ship_speed
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)