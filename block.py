import pygame
from random import randint
from block_type import BlockType

class Block():

    def __init__(self, size, world):
        self.world = world
        self.size = size
        self.regen()

    def regen(self):
        self.block_type = BlockType(randint(0, 7))

        self.x = randint(0, self.world.width - self.block_type.width())
        self.y = -self.block_type.height()

    def move_left(self):
        blocked = False

        for part in self.block_type.parts(self.x, self.y):
            if (part.x == 0 or self.world.blocked_at(part.x - 1, part.y)):
                blocked = True

        if not blocked:
            self.x -= 1

    def move_right(self):
        blocked = False

        for part in self.block_type.parts(self.x, self.y):
            if (part.x == self.world.width - 1 or self.world.blocked_at(part.x + 1, part.y)):
                blocked = True

        if not blocked:
            self.x += 1

    def move_down(self):
        settled = False

        for part in self.block_type.parts(self.x, self.y):
            if part.y >= self.world.height or self.world.blocked_at(part.x, part.y + 1):
                settled = True

        if settled:
            self.settle()
        else:
            self.y += 1

    def settle(self):
        for part in self.block_type.parts(self.x, self.y):
            self.world.set_block_at(part.x, part.y)

        self.regen()

    def update(self):
        self.move_down()

    def draw(self, screen):
        for part in self.block_type.parts(self.x, self.y):
            pygame.draw.rect(screen, (10, 200, 10), (part.x * self.size, part.y * self.size, self.size, self.size))
