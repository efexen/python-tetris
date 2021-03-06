from collections import namedtuple

BlockPart = namedtuple("BlockPart", "x y")

class BlockType():

    block_types = {
        0: {
            'width': 2,
            'height': 2,
            'parts': [(0, 0), (1, 0), (0, 1), (1, 1)]
        },
        1: {
            'width': 2,
            'height': 3,
            'parts': [(0,0), (0, 1), (0, 2), (1, 2)]
        },
        2: {
            'width': 1,
            'height': 4,
            'parts': [(0, 0), (0, 1), (0, 2), (0, 3)]
        },
        3: {
            'width': 3,
            'height': 2,
            'parts': [(1, 0), (2, 0), (0, 1), (1, 1)]
        },
        4: {
            'width': 3,
            'height': 2,
            'parts': [(0, 0), (1, 0), (1, 1), (2, 1)]
        },
        5: {
            'width': 3,
            'height': 2,
            'parts': [(0, 0), (1, 0), (1, 1), (2, 1)]
        },
        6: {
            'width': 2,
            'height': 3,
            'parts': [(1, 0), (1, 1), (1, 2), (0, 2)]
        },
        7: {
            'width': 3,
            'height': 2,
            'parts': [(0, 0), (1, 0), (2, 0), (1, 1)]
        }
    }

    def __init__(self, type_id):
        self.type_id = type_id

    def width(self):
        return self.block_types[self.type_id]['width']

    def height(self):
        return self.block_types[self.type_id]['height']

    def parts(self, origin_x, origin_y):
        for (part_x, part_y) in self.block_types[self.type_id]['parts']:
            yield BlockPart(origin_x + part_x, origin_y + part_y)
