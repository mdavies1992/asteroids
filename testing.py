import pygame
from player import *

# Suppose this is in your main script or a separate testing file
def main():
    pygame.init()
    # Create a Player object at a specific position, e.g., (100, 100)
    player = Player(100, 100)

    # Check its attributes
    print(f"Player position: ({player.x}, {player.y})")
    print(f"Player rotation: {player.rotation}")

main()
