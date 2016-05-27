class World():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._positions = {}

    def set_block_at(self, x, y):
        if self._positions.get(y):
            if not self._positions.get(x):
                self._positions[y][x] = True
        else:
            self._positions[y] = { x: True }

    def blocked_at(self, x, y):
        return self._positions.get(y, {}).get(x, False)
