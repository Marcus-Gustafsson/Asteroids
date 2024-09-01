import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen): #Overridden from parent class
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        else:
            #print("DBG Spawning new asteroids...")

            random_angle = random.uniform(20,50)

            random_dir_one = self.velocity.rotate(random_angle)
            random_dir_two = self.velocity.rotate(-random_angle)

            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            #print("DBG: New radius = ", new_radius)
            first_ast = Asteroid(self.position.x, self.position.y, new_radius)
            first_ast.velocity = random_dir_one * 1.2
            second_ast = Asteroid(self.position.x, self.position.y, new_radius)
            second_ast.velocity = random_dir_two * 1.2




