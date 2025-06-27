from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
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

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # rotates player left when A is pressed
            self.rotate(-dt)
        
        if keys[pygame.K_d]: # rotates player right when D is pressed
            self.rotate(dt)

        if keys[pygame.K_w]: # moves player forward when W is pressed
            self.move(dt)
        
        if keys[pygame.K_s]: # moves player backwards when S is pressed
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt