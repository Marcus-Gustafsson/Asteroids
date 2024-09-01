import circleshape
import constants
import pygame
from main import *

class Player(circleshape.CircleShape):

    def __init__(self, x, y): # Player init method
        super().__init__(x, y, PLAYER_RADIUS) # Calls Circleshape init/constructor with passed arguments
        self.rotation = 0

    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): #Overridden from parent
        color_white = (255,255,255)
        list_of_points = self.triangle()
        line_width = 2

        pygame.draw.polygon(screen, color_white, list_of_points, line_width)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        #print("DBG: keys = ", keys)

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(+dt)


        

