import pygame
from constants import *  # Ensure these include SCREEN_WIDTH and SCREEN_HEIGHT
from circleshape import *  # If needed for CircleShape
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)

        screen.fill((0, 0, 0))  # Proper tuple for color
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Delta time calculation

if __name__ == "__main__":
    main()
