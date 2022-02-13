import pygame
if __name__ == "__main__":
    from bomb import Bomb
else:
    from src.bomb import Bomb

class Player(pygame.sprite.Sprite):
    def __init__(self, startPositionWall, wallSize):
        super().__init__()

        self.wallSize = wallSize
        
        self.positionWall = startPositionWall
        self.positionOnGrill = self.positionWall.gridPosition

        self.size = (40,40)
        self.color = (100,100,100)
        self.speed = 2

        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
                
        self.rect = self.image.get_rect(center=self.positionWall.rect.center)
        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.direction = pygame.math.Vector2(0, 0)
        
        self.key = {"left": pygame.K_q, "right": pygame.K_d, "top": pygame.K_z, "bottom": pygame.K_s, "bomb": pygame.K_SPACE}
        self.keyPressed = {}
        
        self.bombSprites = pygame.sprite.Group()
        self.bombExplosionBlockRange = 3
        self.canAttack = True
                
    def move(self):
        self.direction.x, self.direction.y = 0,0
        if self.keyPressed.get("left"): self.direction.x -= 1
        if self.keyPressed.get("right"): self.direction.x += 1
        if self.keyPressed.get("top"): self.direction.y -= 1
        if self.keyPressed.get("bottom"): self.direction.y += 1

        self.position.x += self.direction.x * self.speed
        self.position.y += self.direction.y * self.speed
        
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def checkCollisions(self, walls):
        collisionsTolerance = 10
        collisions = self.get_hits(walls)
        for wall in collisions:
            if self.direction.x > 0 and abs(wall.rect.left - self.rect.right) < collisionsTolerance: #Moving right
                self.position.x = wall.rect.left - self.rect.w
                self.rect.x = self.position.x
            elif self.direction.x < 0 and abs(wall.rect.right - self.rect.left) < collisionsTolerance: #Moving left
                self.position.x = wall.rect.right
                self.rect.x = self.position.x
            elif self.direction.y > 0 and abs(wall.rect.top - self.rect.bottom) < collisionsTolerance: #Moving down
                self.position.y = wall.rect.top - self.rect.h
                self.rect.y = self.position.y
            elif self.direction.y < 0 and abs(wall.rect.bottom - self.rect.top) < collisionsTolerance: #Moving up
                self.position.y = wall.rect.bottom
                self.rect.y = self.position.y

    def get_hits(self, walls):
        hits = []
        for wall in walls:
            if self.rect.colliderect(wall.rect) and wall.collision == True:
                hits.append(wall)
        return hits

    def attack(self, tick):
        if self.keyPressed.get("bomb") and self.canAttack:
            self.bombSprites.add(Bomb(self.positionWall.rect.center, tick, self.bombExplosionBlockRange*self.wallSize))
            self.canAttack = False

    def pressed(self, keyPressed):
        self.keyPressed = {}
        if keyPressed[self.key["left"]]: self.keyPressed["left"]=True
        if keyPressed[self.key["right"]]: self.keyPressed["right"]=True
        if keyPressed[self.key["top"]]: self.keyPressed["top"]=True
        if keyPressed[self.key["bottom"]]: self.keyPressed["bottom"]=True
        if keyPressed[self.key["bomb"]]: self.keyPressed["bomb"]=True

    def updatePositionOnGrill(self, walls):
        for wall in walls:
            if wall.rect.collidepoint(self.rect.center):
                self.positionOnGrill = wall.gridPosition
                self.positionWall = wall

    def update(self, event, walls, tick):
        keyPressed = pygame.key.get_pressed()        
        self.pressed(keyPressed)

        self.move()
        self.checkCollisions(walls)
        self.updatePositionOnGrill(walls)        
        
        self.attack(tick)        
        self.bombSprites.update(tick)

    def draw(self, surface):
        self.bombSprites.draw(surface)
        surface.blit(self.image, self.rect)