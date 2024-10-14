import pygame
from circleshape import CircleShape
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(surface=screen, 
                            color="white", 
                            points=self.triangle(),
                            width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_s]: 
            self.rotate(-dt)
        if keys[pygame.K_f]:
            self.rotate(dt)
        if keys[pygame.K_e]: 
            self.move(dt)
        if keys[pygame.K_d]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shot(self, dt):
        if self.timer <= 0:
            bullet = Shot(self.position.x, self.position.y)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet.velocity = forward * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
        