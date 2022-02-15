import pygame
from src.explosion import Explosion

class Bomb(pygame.sprite.Sprite):
    def __init__(self, positionWall, currentTick, player):
        super().__init__()

        self.player = player

        self.positionWall = positionWall

        self.size = (20,20)
        self.color = (200,200,200)
        self.explosionRange = 2
        self.timeToExplose = 1 #in second
        self.timeToKill = 1 #in second
        
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)

        self.rect = self.image.get_rect(center=self.positionWall.rect.center)
        self.explosionRect = Explosion(self.explosionRange, self.positionWall)

        self.creationTick = currentTick
        self.explosionTick = 10**100

    def explosion(self, currentTick, wallPositionGrid):
        if (currentTick/1000) - (self.creationTick/1000) >= self.timeToExplose and not self.explosionRect.updateRect:
            self.explosionRect.makeRect(wallPositionGrid)
            self.explosionTick = currentTick
        if (currentTick/1000) - (self.explosionTick/1000) >= self.timeToKill:
            self.explosionRect.kill()
            self.kill()
            self.player.canAttack = True
   
    def update(self, currentTick, wallPositionGrid, surface):
        self.explosion(currentTick, wallPositionGrid)
        self.explosionRect.draw(surface)