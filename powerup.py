import pygame
import random
from constants import *
import circleshape

class PowerUp(circleshape.CircleShape):
    """
    Represents a power-up in the game. 
    Spawns at a random position on the screen with random velocity and direction.
    """

    def __init__(self, image_file, position, velocity, radius=20):
        """
        Initializes the PowerUp sprite with an image, position, and velocity.

        Args:
            image_file (str): Path to the image file for the power-up.
            position (pygame.Vector2): The position where the power-up will spawn.
            velocity (pygame.Vector2): The velocity with which the power-up will move.
            radius (float): The radius of the power-up for collision detection.
        """
        # Initialize CircleShape with position and radius
        super().__init__(position.x, position.y, radius)
        
        # Load power-up image
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))
        self.velocity = velocity  # Set the initial velocity

    def update(self, dt):
        """
        Update the power-up's position based on its velocity.

        Args:
            dt (float): Time delta for smooth movement.
        """
        # Move the power-up based on its velocity and dt
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        self.rect.topleft = (self.position.x, self.position.y)  # Update rect position for rendering

    def draw(self, screen):
        """
        Draws the power-up on the provided Pygame screen surface.
        """
        screen.blit(self.image, self.rect.topleft)

    def is_out_of_bounds(self):
        """
        Check if the power-up is out of bounds (off-screen).

        Returns:
            bool: True if the power-up is out of bounds, False otherwise.
        """
        buffer_zone = 50  # Allow some tolerance before considering it out of bounds
        if (self.rect.x < -buffer_zone or self.rect.x > SCREEN_WIDTH + buffer_zone or
            self.rect.y < -buffer_zone or self.rect.y > SCREEN_HEIGHT + buffer_zone):
            return True
        return False



class PowerUpField(pygame.sprite.Sprite):
    """
    Manages the spawning of a single power-up at a random edge of the screen.
    """

    def __init__(self):
        """
        Initializes the PowerUpField with the power-up's image file.
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image_file = "sprites/PowerUp1.png"  # Store the image file for the power-up
        self.power_up = None  # Placeholder for the spawned power-up

    def spawn_power_up(self):
        """
        Spawns a single power-up at a random edge of the screen with a velocity moving it across the screen.
        """
        # Choose a random edge (0 = left, 1 = right, 2 = top, 3 = bottom)
        edge = random.choice([0, 1, 2, 3])

        # Determine position and velocity based on which edge
        if edge == 0:  # Left edge
            position = pygame.Vector2(-50, random.uniform(0, SCREEN_HEIGHT))
            velocity = pygame.Vector2(random.uniform(50, 100), 0)  # Move right
        elif edge == 1:  # Right edge
            position = pygame.Vector2(SCREEN_WIDTH + 50, random.uniform(0, SCREEN_HEIGHT))
            velocity = pygame.Vector2(-random.uniform(50, 100), 0)  # Move left
        elif edge == 2:  # Top edge
            position = pygame.Vector2(random.uniform(0, SCREEN_WIDTH), -50)
            velocity = pygame.Vector2(0, random.uniform(50, 100))  # Move down
        elif edge == 3:  # Bottom edge
            position = pygame.Vector2(random.uniform(0, SCREEN_WIDTH), SCREEN_HEIGHT + 50)
            velocity = pygame.Vector2(0, -random.uniform(50, 100))  # Move up

        # Step 3: Spawn the power-up
        self.power_up = PowerUp(self.image_file, position, velocity)

    def update(self, dt):
        """
        Updates the PowerUpField, handling the spawning and movement of the power-up.

        Args:
            dt (float): Time delta for smooth movement and spawn timer updates.
        """
        # If there's no active power-up, spawn one
        if self.power_up is None:
            self.spawn_power_up()

        # If the power-up exists, update its position
        if self.power_up:
            self.power_up.update(dt)

            # Check if the power-up is out of bounds
            if self.power_up.is_out_of_bounds():
                self.power_up.kill()  # Remove the current power-up from all groups
                self.power_up = None  # Mark the current power-up as None so a new one can be spawned



