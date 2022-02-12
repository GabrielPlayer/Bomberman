import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, map, size,pos) :
        super().__init__()
        self.map = map
        
        self.color = (200,222,0)
        
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
        self.collision = True

class AirWall(Wall):
    def __init__(self, map, size, pos):
        super().__init__(map, size, pos)

        self.color = (0,100,0)

        self.image.fill(self.color)

        self.collision = False

class UnbreakableWall(Wall):
    def __init__(self, map, size, pos):
        super().__init__(map, size, pos)
        
        self.color = (200,0,0)
        
        self.image.fill(self.color)


class BreakeableWall(Wall):
    def __init__(self, map, size, pos):
        super().__init__(map, size, pos)
        
        self.color = (0,0,200)
        
        self.image.fill(self.color)