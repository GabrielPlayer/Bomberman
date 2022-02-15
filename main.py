import pygame
from src.map import Map
from src.player import Player

class Main:
    def __init__(self):
        pygame.init()
        self.screenSize = (800,800)
        self.FPS = 60

        self.screen = pygame.display.set_mode(self.screenSize)
        self.clock, self.dt = pygame.time.Clock(), 0

        self.backgroundColor = (0,0,0)

        self.map = Map(self)
        self.map.loadWall()

        self.player = Player(self.map.positionGrid[11][1])

        self.isRun = False
        self.fullscreen = False

    def run(self):
        self.isRun = True
        
        while self.isRun:
            self.screen.fill(self.backgroundColor)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.isRun = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        if not self.fullscreen:
                            self.fullscreen = True
                            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                        else:
                            self.fullscreen = False
                            self.screen = pygame.display.set_mode(self.screenSize)
                    elif event.key == pygame.K_F5:
                        self.map.image.fill(self.map.backgroundColor)
                        self.map.loadWall()

            self.map.draw(self.screen)
            self.map.wallSprites.draw(self.map.image)

            self.player.update(events, self.map.wallSprites.sprites(), pygame.time.get_ticks())
            self.player.bombSprites.update(pygame.time.get_ticks(), self.map.positionGrid, self.map.image)
            self.player.draw(self.map.image)
            self.player.bombSprites.draw(self.map.image)

            pygame.display.update()
            self.clock.tick(self.FPS)
            pygame.display.set_caption(str(int(self.clock.get_fps())))

if __name__ == "__main__":
    main = Main()
    main.run()