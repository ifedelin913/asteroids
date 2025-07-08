import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, 
                           self.radius, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)

    # used to split asteroids upon being shot, larger asteroids will
    # be split in two and smaller asteroids will simply disappear
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)

        # angles are opposite of each other so the new asteroids drift
        # in opp directions
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        # since the asteroids are smaller, the velocity is scaled up
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2
