import pygame
from random import randint

class Block():

    def __init__(self, size, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height
        self.size = size
        self.x = randint(0, world_width - 1)
        self.y = -1
        self.active = True

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_right(self):
        if self.x < self.world_width - 1:
            self.x += 1

    def update(self):
        self.y += 1

        if self.y >= self.world_height:
            self.active = False

    def draw(self, screen):
        pygame.draw.rect(screen, (10, 200, 10), (self.x * self.size, self.y * self.size, self.size, self.size))
