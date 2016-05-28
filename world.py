import pygame

class World():

    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self._positions = {}

    def set_block_at(self, x, y):
        if self._positions.get(y):
            if not self._positions.get(x):
                self._positions[y][x] = True
        else:
            self._positions[y] = { x: True }

        self.check_row(y)

    def check_row(self, y):
        if len(self._positions.get(y)) == 10:
            del self._positions[y]

            self._positions = dict(map(lambda (k, v): (k + 1, v), self._positions.iteritems()))

    def blocked_at(self, x, y):
        return self._positions.get(y, {}).get(x, False)

    def draw(self, screen):
        for y, xses in self._positions.iteritems():
            for x in xses:
                pygame.draw.rect(screen, (10, 200, 10), (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
