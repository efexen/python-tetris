import pygame
from random import randint
from block_type import BlockType

class Block():

    def __init__(self, size, world):
        self.world = world
        self.size = size
        self.regen()

    def regen(self):
        self.block_type = BlockType(randint(0, 1))

        self.x = randint(0, self.world.width - self.block_type.width())
        self.y = -self.block_type.height()

    def move_left(self): # update to check parts
        if (self.x > 0 and not self.world.blocked_at(self.x - 1, self.y)):
            self.x -= 1

    def move_right(self): # update to check parts
        if (self.x < self.world.width - self.block_type.width() and not self.world.blocked_at(self.x + 1, self.y)):
            self.x += 1

    def move_down(self): # update to check parts
        if self.y >= (self.world.height - (self.block_type.height() - 1)):
            self.settle()
            return

        if self.world.blocked_at(self.x, self.y + 1):
            self.settle()
            return

        self.y += 1

    def settle(self):
        for (offset_x, offset_y) in self.block_type.parts():
            self.world.set_block_at(self.x + offset_x, self.y + offset_y)

        self.regen()

    def update(self):
        self.move_down()
        print(self.world._positions)

    def draw(self, screen):
        for (offset_x, offset_y) in self.block_type.parts():
            pygame.draw.rect(screen, (10, 200, 10), ((self.x + offset_x) * self.size, (self.y + offset_y) * self.size, self.size, self.size))
