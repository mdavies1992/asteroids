from circleshape import CircleShape  # Import only what's needed, if possible
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.math.Vector2(0, 0)  # Initial velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        color = (255, 255, 255)  # White color
        pygame.draw.circle(screen, color, (self.position.x, self.position.y), self.radius, 2)
