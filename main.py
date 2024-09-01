import pygame
from player import Player, Shoot
from asteroid import Asteroid
from constants import *
from asteroidfield import AsteroidField

def main():
    """
    Main game loop for the Asteroids game.

    This function initializes the game, sets up the screen, groups, and entities, 
    and runs the main game loop that handles events, updates, collision checks, 
    drawing, and frame rate control.
    """
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # Initialize Pygame and set up the display window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    # Create sprite groups for updating and drawing entities
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shoot_group = pygame.sprite.Group()

    # Assign containers to each class for grouping
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shoot.containers = (shoot_group, updatable_group, drawable_group)

    # Instantiate the player and asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0  # Delta time for frame rate control

    keep_going = True
    while keep_going:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop

        # Update all sprites
        for update in updatable_group:
            update.update(dt)

        # Collision detection
        for asteroid in asteroids_group:
            if asteroid.collision_check(player):
                print("Game over!")
                pygame.quit()  # Exit the game if player collides with an asteroid
            for bullet in shoot_group:
                if asteroid.collision_check(bullet):
                    bullet.kill()
                    asteroid.split()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw all sprites
        for draw in drawable_group:
            draw.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control the frame rate and calculate delta time
        dt = game_clock.tick(60) / 1000  # 60 FPS (milliseconds to seconds conversion)

if __name__ == "__main__":
    main()
