import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, explosionRange, positionWall):
        super().__init__()
        
        self.explosionRange = explosionRange
        self.positionWall = positionWall
        self.gridPosition = self.positionWall.gridPosition
        
        self.color = (0,0,0,0)
        
        self.leftRect = pygame.Rect(0,0,0,0)
        self.rightRect = pygame.Rect(0,0,0,0)
        self.topRect = pygame.Rect(0,0,0,0)
        self.bottomRect = pygame.Rect(0,0,0,0)
        
        self.updateRect = False
        
        self.explosionDispersal = {"left":self.explosionRange, "right":self.explosionRange, "top":self.explosionRange, "bottom":self.explosionRange}
        self.explosionRectRange = {"left":self.explosionRange, "right":self.explosionRange, "top":self.explosionRange, "bottom":self.explosionRange}
    
    def checkSpaceAround(self,wallPositionGrid):
        if self.gridPosition[0] < self.explosionRange: #Checking left
            self.explosionDispersal["left"] = self.gridPosition[0]
        if (len(wallPositionGrid[0])-1)-self.gridPosition[0] < self.explosionRange : #Checking right
            self.explosionDispersal["right"] = (len(wallPositionGrid[0])-1)-self.gridPosition[0]        
        if self.gridPosition[1] < self.explosionRange: #Checking top
            self.explosionDispersal["top"] = self.gridPosition[1]
        if (len(wallPositionGrid)-1)-self.gridPosition[1] < self.explosionRange : #Checking bottom
            self.explosionDispersal["bottom"] = (len(wallPositionGrid)-1)-self.gridPosition[1]            

    def checkWallAround(self, wallPositionGrid):
        self.checkSpaceAround(wallPositionGrid)
        modif = [0,0,0,0]
        for i in range(1,self.explosionRange+1):
            if i <= self.explosionDispersal["left"] and modif[0]==0 and wallPositionGrid[self.gridPosition[1]][self.gridPosition[0]-i].collision:
                self.explosionRectRange["left"] = i-1
                modif[0] = 1
            if i <= self.explosionDispersal["right"] and modif[1]==0 and wallPositionGrid[self.gridPosition[1]][self.gridPosition[0]+i].collision:
                self.explosionRectRange["right"] = i-1
                modif[1] = 1
            if i <= self.explosionDispersal["top"] and modif[2]==0 and wallPositionGrid[self.gridPosition[1]-i][self.gridPosition[0]].collision:
                self.explosionRectRange["top"] = i-1
                modif[2] = 1
            if i <= self.explosionDispersal["bottom"] and modif[3]==0 and wallPositionGrid[self.gridPosition[1]+i][self.gridPosition[0]].collision:
                self.explosionRectRange["bottom"] = i-1
                modif[3] = 1

    def makeRect(self, wallPositionGrid):
        self.updateRect = True
        self.checkWallAround(wallPositionGrid)
        if self.explosionRectRange["left"] > 0: #making left
            x = wallPositionGrid[self.gridPosition[1]][self.gridPosition[0]-self.explosionRectRange["left"]].rect.x
            y = self.positionWall.rect.y
            w = self.positionWall.size[0]*(self.explosionRectRange["left"]+1)
            h = self.positionWall.size[1]
            self.leftRect = pygame.Rect(x,y,w,h)
        if self.explosionRectRange["left"] < self.explosionRange and wallPositionGrid[self.gridPosition[1]][self.gridPosition[0]-self.explosionRectRange["left"]-1].breakable:
            wallPositionGrid[self.gridPosition[1]][self.gridPosition[0]-self.explosionRectRange["left"]-1].kill()

        if self.explosionRectRange["right"] > 0: #making right
            x = wallPositionGrid[self.gridPosition[1]][self.gridPosition[0]].rect.x
            y = self.positionWall.rect.y
            w = self.positionWall.size[0]*(self.explosionRectRange["right"]+1)
            h = self.positionWall.size[1]
            self.rightRect = pygame.Rect(x,y,w,h)
        if self.explosionRectRange["right"] < self.explosionRange and wallPositionGrid[self.gridPosition[1]][self.gridPosition[0]+self.explosionRectRange["right"]+1].breakable:
            wallPositionGrid[self.gridPosition[1]][self.gridPosition[0]+self.explosionRectRange["right"]+1].kill()

        if self.explosionRectRange["top"] > 0: #making top
            x = self.positionWall.rect.x
            y = wallPositionGrid[self.gridPosition[1]-self.explosionRectRange["top"]][self.gridPosition[0]].rect.y
            w = self.positionWall.size[0]
            h = self.positionWall.size[1]*(self.explosionRectRange["top"]+1)
            self.topRect = pygame.Rect(x,y,w,h)
        if self.explosionRectRange["top"] < self.explosionRange and wallPositionGrid[self.gridPosition[1]-self.explosionRectRange["top"]-1][self.gridPosition[0]].breakable:
            wallPositionGrid[self.gridPosition[1]-self.explosionRectRange["top"]-1][self.gridPosition[0]].kill()

        if self.explosionRectRange["bottom"] > 0: #making bottom
            x = self.positionWall.rect.x
            y = wallPositionGrid[self.gridPosition[1]][self.gridPosition[0]].rect.y
            w = self.positionWall.size[0]
            h = self.positionWall.size[1]*(self.explosionRectRange["bottom"]+1)
            self.bottomRect = pygame.Rect(x,y,w,h)
        if self.explosionRectRange["bottom"] < self.explosionRange and wallPositionGrid[self.gridPosition[1]+self.explosionRectRange["bottom"]+1][self.gridPosition[0]].breakable:
            wallPositionGrid[self.gridPosition[1]+self.explosionRectRange["bottom"]+1][self.gridPosition[0]].kill()

    def draw(self, surface):        
        pygame.draw.rect(surface, self.color, self.leftRect)
        pygame.draw.rect(surface, self.color, self.rightRect)
        pygame.draw.rect(surface, self.color, self.topRect)
        pygame.draw.rect(surface, self.color, self.bottomRect)