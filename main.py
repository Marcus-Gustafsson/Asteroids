# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import player

from constants import *


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0 # Delta
    player_one = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    keep_going = True

    while keep_going:

        screen.fill((0,0,0))
        player_one.draw(screen)

        player_one.update(dt)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        


        pygame.display.flip()


        dt = (game_clock.tick(60)/1000) # 60 fps (waits a 1/60th second before updating), "1000" --> 1000 ms


if __name__ == "__main__":
    main()