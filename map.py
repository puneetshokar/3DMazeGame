import pygame
import mapgeneration

_ = False

mini_map = mapgeneration.make_maze(16,9,(0,1),(8,14))

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mapgeneration.make_maze(16,9,(1,1),(7,14))
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value != '_':
                    self.world_map[(i,j)] = value
    
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
