# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from constants import *
from asteroidfield import AsteroidField


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    dt = 0 # Delta


    keep_going = True
    while keep_going:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        for update in updatable_group:
            update.update(dt)

        for asteroid in asteroids_group:
           if asteroid.collision_check(player):
               print("Game over!")
               pygame.quit()aaaaaa

        screen.fill((0,0,0))


        for draw in drawable_group:
            draw.draw(screen)        


        pygame.display.flip()


        dt = (game_clock.tick(60)/1000) # 60 fps (waits a 1/60th second before updating), "1000" --> 1000 ms


if __name__ == "__main__":
    main()