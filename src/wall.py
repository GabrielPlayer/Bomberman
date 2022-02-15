import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, map, size, pos, gridPosition) :
        super().__init__()
        self.wallType = "init"
        
        self.map = map
        self.gridPosition = gridPosition
        
        self.color = (200,222,0)
        self.pos = pos
        self.size = size
        
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
        self.collision = True
        self.breakable = True
        
    def __str__(self):
        text = f"\ncollision: {self.collision}\nbreakable: {self.breakable}\ngridPosition: {self.gridPosition}\ntype: {self.wallType}\ncolor: {self.color}"
        return text
        
class AirWall(Wall):
    def __init__(self, map, size, pos, gridPosition):
        super().__init__(map, size, pos, gridPosition)
        self.wallType = "air"
        self.color = (0,100,0)

        self.image.fill(self.color)

        self.collision = False

class UnbreakableWall(Wall):
    def __init__(self, map, size, pos, gridPosition):
        super().__init__(map, size, pos, gridPosition)
        self.wallType = "unbreakable"
        
        self.color = (200,0,0)
        
        self.image.fill(self.color)
        
        self.breakable = False

class BreakeableWall(Wall):
    def __init__(self, map, size, pos, gridPosition):
        super().__init__(map, size, pos, gridPosition)
        self.wallType = "breakable"
                
        self.color = (0,0,200)
        
        self.image.fill(self.color)        
    
    def kill(self):
        self.map.wallSprites.remove(self)
        newWall = AirWall(self,self.size,self.pos, self.gridPosition)
        self.map.wallSprites.add(newWall)
        self.map.positionGrid[self.gridPosition[1]][self.gridPosition[0]] = newWall
        return super().kill()