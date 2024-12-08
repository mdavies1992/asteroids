import pygame
from constants import *  # Ensure these include SCREEN_WIDTH and SCREEN_HEIGHT
from circleshape import *  # If needed for CircleShape
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import *
import sys

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    dt = 0
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game Over!")
                sys.exit()

        screen.fill((0, 0, 0))  # Proper tuple for color

        for sprite in drawable:
            sprite.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Delta time calculation

if __name__ == "__main__":
    main()
