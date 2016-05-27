import pygame
from pygame.locals import *
from block import Block
from world import World

class Tetris:

    def __init__(self):
        pygame.init()

        self.set_sizes()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.blocks = []

        self.new_block()

        self.running = True
        self.frame_counter = 0
        self.difficulty = 30

    def set_sizes(self):
        world_width = 10

        display_info = pygame.display.Info()
        candidate_width = int(display_info.current_h * 0.5)

        self.width = (candidate_width // world_width) * world_width
        self.height = (int(display_info.current_h * 0.8) // world_width) * world_width

        self.block_size = self.width / world_width
        world_height = self.height / self.block_size

        self.world = World(world_width, world_height)

    def new_block(self):
        self.active_block = Block(self.block_size, self.world)
        self.blocks.append(self.active_block)

    def check_events(self):
        for event in pygame.event.get():
            self.handle_event(event)

    def quit(self, _event):
        self.running = False

    def keydown(self, event):
        if event.key == K_LEFT:
            self.active_block.move_left()
        elif event.key == K_RIGHT:
            self.active_block.move_right()
        elif event.key == K_DOWN:
            self.active_block.move_down()
        elif event.key == K_ESCAPE:
            self.quit(event)

    def handle_event(self, event):
        {
            QUIT: self.quit,
            KEYDOWN: self.keydown
        }.get(event.type, lambda _: None)(event)

    def update(self):
        for block in self.blocks:
            if block.active:
                block.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        for block in self.blocks:
            block.draw(self.screen)

        pygame.display.flip()

    def check_state(self):
        if not self.active_block.active:
            self.new_block()

    def play(self):
        while(self.running):
            self.check_events()

            if self.frame_counter % self.difficulty == 0:
                self.update()

            self.check_state()
            self.draw()
            self.clock.tick(60)
            self.frame_counter += 1

game = Tetris()
game.play()
