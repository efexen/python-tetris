import pygame
from random import randint

class Block():

    def __init__(self, size, world):
        self.world = world
        self.size = size
        self.x = randint(0, world.width - 1)
        self.y = -1
        self.active = True

    def move_left(self):
        if (self.x > 0 and not self.world.blocked_at(self.x - 1, self.y)):
            self.x -= 1

    def move_right(self):
        if (self.x < self.world.width - 1 and not self.world.blocked_at(self.x + 1, self.y)):
            self.x += 1

    def move_down(self):
        if self.y >= self.world.height:
            self.settle()
            return

        if self.world.blocked_at(self.x, self.y + 1):
            self.settle()
            return

        self.y += 1

    def settle(self):
        self.active = False
        self.world.set_block_at(self.x, self.y)

    def update(self):
        self.move_down()
        print(self.world._positions)

    def draw(self, screen):
        pygame.draw.rect(screen, (10, 200, 10), (self.x * self.size, self.y * self.size, self.size, self.size))
