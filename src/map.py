import pygame
if __name__ == "__main__":
    from wall import *
else:
    from src.wall import *

class Map(pygame.sprite.Sprite):
    def __init__(self, main) :
        super().__init__()
        self.main = main

        self.backgroundColor = (0,222,0)
        
        self.image = pygame.Surface(self.main.screenSize)
        self.image.fill(self.backgroundColor)

        self.rect = self.image.get_rect()

        self.wallSize = (55,55)
        self.wallSprites = pygame.sprite.Group()

        self.positionGrid = []

        self.mapFilePath = "src/mapCode.txt"

    def loadWall(self):
        self.positionGrid = []
        self.wallSprites.empty()
        listWall = self.loadFile()
        y=0
        for i in range(len(listWall)):
            line = []
            x=0
            for j in range(len(listWall[i])):
                char = listWall[i][j]
                if char == "0":
                    wall = AirWall(self, self.wallSize, (x,y), (i,j))
                elif char == "1":
                    wall = BreakeableWall(self, self.wallSize, (x,y), (i,j))
                elif char == "2":
                    wall = UnbreakableWall(self, self.wallSize, (x,y), (i,j))
                else:
                    wall = Wall(self, self.wallSize, (x,y), (i,j))
                self.wallSprites.add(wall)
                x+=self.wallSize[0]
                line.append(wall)
            y+=self.wallSize[1]
            self.positionGrid.append(line)

    def loadFile(self):
        listeMap = []
        with open(self.mapFilePath, "r") as file:
            for l in file.readlines():
                if l[-1] == "\n": l = l[:-1]
                listeMap.append(l)
        return listeMap
      
    def draw(self, surface):
        surface.blit(self.image, self.rect)