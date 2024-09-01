import circleshape
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen): #Overridden from parent class
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    
    def update(self, dt):
        self.position += self.velocity * dt
