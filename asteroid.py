import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    """
    A class representing an asteroid in the game, inheriting from CircleShape.

    The Asteroid class extends the CircleShape base class to include specific functionality 
    such as drawing, updating position, and splitting into smaller asteroids.
    """

    def __init__(self, x, y, radius):
        """
        Initializes an Asteroid instance with a specified position and radius.

        Args:
            x (float): The x-coordinate of the asteroid's center.
            y (float): The y-coordinate of the asteroid's center.
            radius (float): The radius of the asteroid.
        """
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draws the asteroid on the provided Pygame screen surface.

        Overrides the draw method in CircleShape. It draws the asteroid as 
        a white circle with a specified radius and a border width

        Args:
            screen (pygame.Surface): The Pygame surface where the asteroid will be drawn.
        """
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        """
        Updates the asteroid's position based on its velocity and the time delta.

        Overrides the update method in CircleShape. It moves the asteroid 
        by updating its position with respect to the time passed (`dt`) and its velocity.

        Args:
            dt (float): The time delta, representing the time passed since the last update.
        """
        self.position += self.velocity * dt

    def split(self):
        """
        Splits the asteroid into two smaller asteroids if its radius exceeds the minimum size.

        Removes the current asteroid from the game. 
        If the asteroid's radius is greater than the minimum defined in `constants.ASTEROID_MIN_RADIUS`, 
        it creates two smaller asteroids with a reduced radius, moving in slightly different 
        directions based on a random angle.

        The newly created asteroids inherit their position from the original asteroid but 
        have adjusted velocities.
        """
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            random_dir_one = self.velocity.rotate(random_angle)
            random_dir_two = self.velocity.rotate(-random_angle)

            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

            first_ast = Asteroid(self.position.x, self.position.y, new_radius)
            first_ast.velocity = random_dir_one * 1.2
            second_ast = Asteroid(self.position.x, self.position.y, new_radius)
            second_ast.velocity = random_dir_two * 1.2





