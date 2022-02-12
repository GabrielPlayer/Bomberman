import pygame

class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos, currentTick, explosionRange):
        super().__init__()

        self.size = (20,20)
        self.color = (200,200,200)
        self.explosionRange = explosionRange
        self.timeToExplose = 3 #in second

        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)

        self.rect = self.image.get_rect(center=pos)

        self.creationTick = currentTick

    def explosion(self, currentTick):        
        if (currentTick/1000) - (self.creationTick/1000) >= self.timeToExplose:
            self.kill()
            print(self.explosionRange)
            
    def update(self, currentTick):
        self.explosion(currentTick)