import pygame
class Player:
    def __init__(self, x, y):
        self.SIZE = (40, 40)
        # creando el rectangulo de nuestro jugador
        self.rect = pygame.Rect(x, y, self.SIZE[0], self.SIZE[1])

        self.x = x
        self.y = y
        # velocidad y direccion del jugador.
        self.change_x = 0
        self.change_y = 0
        self.speed = 10
        # attributos para las diferentes teclas
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        # estetica
        self.color = (240, 240, 240)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        self.change_x, self.change_y = 0, 0
        # actualizar la velocidad y el cambio de l

        # actualizando el cambio de X
        if self.left and not self.right:
            self.change_x = -self.speed
        if self.right and not self.left:
            self.change_x = self.speed

        # actualizando el cambio de Y
        if self.up and not self.down:
            self.change_y = -self.speed
        if self.down and not self.up:
            self.change_y = self.speed

        # aplicar los cambios realizados
        self.x += int(self.change_x)
        self.y += int(self.change_y)
        # actualizar el rectangulo
        self.rect = pygame.Rect(self.x, self.y, self.SIZE[0], self.SIZE[1])
