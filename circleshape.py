import pygame

class CircleShape(pygame.sprite.Sprite):
    """
    Base class for game objects that represent circular shapes in a Pygame environment.

    Attributes:
        position (pygame.Vector2): The position of the circle's center.
        velocity (pygame.Vector2): The velocity of the circle.
        radius (float): The radius of the circle.
    """

    def __init__(self, x, y, radius):
        """
        Initializes the CircleShape with a given position and radius.

        Args:
            x (float): The x-coordinate of the circle's center.
            y (float): The y-coordinate of the circle's center.
            radius (float): The radius of the circle.
        """
        # We will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Sub-classes must override
        raise NotImplementedError("Subclass must implement")

    def update(self, dt):
        # Sub-classes must override
        raise NotImplementedError("Subclass must implement")

    def collision_check(self, circleShape):
        """
        Checks for a collision with another CircleShape instance.

        Args:
            circleShape (CircleShape): Another instance of CircleShape to check for collision.

        Returns:
            bool: True if the two circles collide, otherwise False.
        """
        r1_r2 = self.radius + circleShape.radius
        if self.position.distance_to(circleShape.position) <= r1_r2:
            return True
        else:
            return False
