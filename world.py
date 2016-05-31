import pygame

class World():

    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self._positions = {}

    def set_block_at(self, x, y):
        if self._positions.get(y):
            if not self._positions[y].get(x):
                self._positions[y][x] = True
        else:
            self._positions[y] = { x: True }

        self.check_row(y)

    def increment_keys_above(self, current_key, key, values):
        if key < current_key:
            return (key + 1, values)
        else:
            return (key, values)

    def check_row(self, y):
        if len(self._positions.get(y)) == 10:
            del self._positions[y]

            self._positions = dict(map(lambda (k, v): self.increment_keys_above(y, k, v), self._positions.iteritems()))

    def blocked_at(self, x, y):
        return self._positions.get(y, {}).get(x, False)

    def draw(self, screen):
        for y, xses in self._positions.iteritems():
            for x in xses:
                pygame.draw.rect(screen, (10, 200, 10), (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
