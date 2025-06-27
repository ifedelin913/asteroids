from circleshape import CircleShape
from constants import PLAYER_RADIUS
import pygame

class Player(CircleShape): # class player extends CircleShape
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) #call parent constructor
        self.rotation = 0

    def triangle(self): # sets player point information for drawing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    # draw the player to the screen
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)