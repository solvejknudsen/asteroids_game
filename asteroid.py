import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def polygon(self):
        coords = []
        edges = 5
        for i in range(0, edges):
            coords.append(
                self.position
                + pygame.Vector2(0, 1).rotate(self.rotation + i * (360 / edges))
                * self.radius
            )
        return coords

    def draw(self, screen):
        # param: surface to draw on, color, center pos, radius, line width
        pygame.draw.polygon(screen, "white", self.polygon(), LINE_WIDTH)

    #    def rotate(self, dt):
    #        rot_angle = 1
    #        self.rotation += rot_angle * dt

    def update(self, dt):
        self.position += self.velocity * dt

    #        self.position += pygame.Vector2(0.1).rotate(self.rotation + rot_angle) * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_asteroid_vel_1 = self.velocity.rotate(angle)
        new_asteroid_vel_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_asteroid_vel_1 * 1.2
        new_asteroid_2.velocity = new_asteroid_vel_2 * 1.2
