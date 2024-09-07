import circleshape
import constants
import pygame

class Player(circleshape.CircleShape):
    """
    Represents the player-controlled spaceship in the game.

    The Player class handles movement, rotation, shooting, and drawing the player 
    ship on the screen. It inherits from the CircleShape base class.
    """

    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0.3
        self.original_shot_timer = self.shot_timer  # Store the original shot timer
        self.power_up_timer = 0  # Initialize power-up timer to 0

    def triangle(self):
        """
        Computes the points of the triangle representing the player's ship.

        The player's ship is visualized as a triangle that points in the direction 
        of movement. This method calculates the vertices of that triangle based on 
        the player's position and rotation.

        Returns:
            list[pygame.Vector2]: A list of three points defining the triangle's vertices.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """
        Draws the player ship as a triangle on the provided Pygame screen surface.

        This method overrides the draw method in CircleShape and renders the player 
        as a white triangle with a line width of 2 pixels.

        Args:
            screen (pygame.Surface): The Pygame surface where the player will be drawn.
        """
        color_white = (255, 255, 255)
        list_of_points = self.triangle()
        line_width = 2

        pygame.draw.polygon(screen, color_white, list_of_points, line_width)

    def rotate(self, dt):
        """
        Rotates the player ship based on the time delta.

        Adjusts the player's rotation angle by a rate defined in constants.

        Args:
            dt (float): The time delta since the last update.
        """
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        """
        Moves the player ship forward or backward based on its current rotation.

        The player's position is updated in the direction it is currently facing.

        Args:
            dt (float): The time delta since the last update.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        """
        Creates a Shoot instance representing a bullet fired from the player.

        The bullet is fired in the direction the player is facing and at a speed 
        defined in constants.
        """
        shot = Shoot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED

    def update(self, dt):
        """
        Updates the player state based on user input and handles power-up effects.
        """
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        # Check if the power-up timer is active
        if self.power_up_timer > 0:
            self.power_up_timer -= dt
            if self.power_up_timer <= 0:
                # Reset the shot_timer to the original value after X seconds
                self.shot_timer = self.original_shot_timer

        if keys[pygame.K_w]:
            self.move(+dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(+dt)

        if keys[pygame.K_SPACE]:
            if self.shot_timer <= 0:
                self.shoot()
                # Check if the power-up timer is active
                if self.power_up_timer > 0:
                    self.power_up_timer -= dt
                    self.shot_timer = 0.005  # Set shot_timer to faster shooting
                    if self.power_up_timer <= 0:
                        self.shot_timer = self.original_shot_timer
                else:
                    self.shot_timer = self.original_shot_timer

    def apply_power_up(self):
        """
        Apply the power-up effect: reduce the shot_timer and set the power-up timer.
        """
        self.power_up_timer = 2  # Power-up effect lasts for X seconds


class Shoot(circleshape.CircleShape):
    """
    Represents a projectile shot by the player in the game.

    The Shoot class handles the creation, movement, and rendering of bullets fired 
    by the player, inheriting from the CircleShape base class.
    """

    def __init__(self, x, y):
        """
        Initializes a bullet at a given position with a predefined radius.

        Args:
            x (float): The x-coordinate of the bullet's starting position.
            y (float): The y-coordinate of the bullet's starting position.
        """
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen):
        """
        Draws the bullet as a small circle on the provided Pygame screen surface.

        This method overrides the draw method in CircleShape and renders the bullet 
        as a white circle with a line width of 2 pixels.

        Args:
            screen (pygame.Surface): The Pygame surface where the bullet will be drawn.
        """
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        """
        Updates the bullet's position based on its velocity and the time delta.

        The bullet moves in the direction it was fired until it goes off-screen 
        or hits a target.

        Args:
            dt (float): The time delta since the last update.
        """
        self.position += self.velocity * dt








        

