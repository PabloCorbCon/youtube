import pygame
from player import Player
pygame.init()

def main():
    # ================ CONSTANTES =======================
    WIDTH, HEIGHT = 600, 600
    SIZE = (WIDTH, HEIGHT)
    TITLE = 'Movimiento fluido en Pygame'
    CLOCK = pygame.time.Clock()
    MAX_FPS = 120
    # ================== Pantalla ======================
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(TITLE)
    # ================== Jugador =======================
    player = Player(SIZE[0]//2, SIZE[1]//2)
    # ================== Main loop =====================
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print('UP')
                    player.up = True
                if event.key == pygame.K_DOWN:
                    print('DOWN')
                    player.down = True
                if event.key == pygame.K_LEFT:
                    print('LEFT')
                    player.left = True
                if event.key == pygame.K_RIGHT:
                    print('RIGHT')
                    player.right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.up = False
                if event.key == pygame.K_DOWN:
                    player.down = False
                if event.key == pygame.K_LEFT:
                    player.left = False
                if event.key == pygame.K_RIGHT:
                    player.right = False


        screen.fill((40, 40, 40))
        # actualizar elementos
        player.draw(screen)
        player.update()
        
        pygame.display.flip()
        CLOCK.tick(MAX_FPS)
if __name__ == '__main__':
    main()
