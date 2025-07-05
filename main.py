import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # create groups for updatables, drawables, and asteroids
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # add respective groups to static conntainers of Classes
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Player.containers = (updatables, drawables)

    # create Player and AsteroidField objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    running = True

    while running: # game loop
        clock = pygame.time.Clock()
        dt = clock.tick(60) / 1000
        updatables.update(dt) #update using updatables group
        player.shots.update(dt) # update the shots group

        # collision detection loop
        for asteroid in asteroids:
            if player.collision(asteroid) == True:
                print("Game Over!")
                sys.exit(0)

        # loop controls quit logic during runtime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # set screen color as black and draw all objects in drawables group
        screen.fill((0, 0, 0))
        for drawable in drawables:
            drawable.draw(screen)
        
        # draw shots
        for shot in player.shots:
            shot.draw(screen)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
