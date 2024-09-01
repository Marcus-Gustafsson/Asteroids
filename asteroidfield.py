import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):
    """
    Manages the spawning of asteroids from random edges of the screen in a game.

    The AsteroidField class handles the logic for creating asteroids at random edges 
    of the screen and controlling their movement into the play area.
    """

    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]
    """
    Predefined screen edges and associated spawning logic.

    This attribute defines four edges around the screen and the corresponding logic to 
    determine where asteroids will appear and what direction they will travel.
    """

    def __init__(self):
        """
        Initializes an AsteroidField instance.

        Sets up the initial spawn timer for controlling the asteroid spawn rate.
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """
        Spawns a new asteroid at a specified position with a given radius and velocity.

        Args:
            radius (float): The radius of the asteroid.
            position (pygame.Vector2): The position where the asteroid will spawn.
            velocity (pygame.Vector2): The velocity with which the asteroid will move.
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        """
        Updates the asteroid field, spawning new asteroids at intervals.

        The method checks if the spawn timer has exceeded the spawn rate and 
        then spawns a new asteroid at a random edge with random speed and direction.

        Args:
            dt (float): The time delta since the last update.
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # Spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
