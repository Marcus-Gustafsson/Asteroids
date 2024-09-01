import circleshape
import constants
import pygame

class Player(circleshape.CircleShape):

    def __init__(self, x, y): # Player init method
        super().__init__(x, y, constants.PLAYER_RADIUS) # Calls Circleshape init/constructor with passed arguments
        self.rotation = 0
        self.shot_timer = 0
    
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
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    def shoot(self):
        shot = Shoot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED


    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt
        #print("DBG: keys = ", keys)

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
                self.shot_timer = constants.PLAYER_SHOOT_COOLDOWN



class Shoot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)

    
    def draw(self, screen): #Overridden from parent class
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    
    def update(self, dt):
        self.position += self.velocity * dt







        

