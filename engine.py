from player import Player
from enemy import Enemy
from wall import Wall
from laser import LaserP

class Collisions:

    def __init__(self, canvas):
        self.canvas = canvas
        self.player = Player(self.canvas)
        self.enemy = Enemy(self.canvas)
        self.wall = Wall(self.canvas)
        self.playerCoords = self.player.playerCoords()
        self.laser = LaserP(self.canvas, self.playerCoords)



        self.collisionLaserwall(self.laser, self.wall)
        self.canvas.after(50, self.collisionLaserwall(self.laser, self.wall))

    def collisionLaserwall(self, laser, wall):
        x1, y1 = self.canvas.coords(laser)

        for x in self.wall.createWalls():
            x2, y2 = self.canvas.coords(x)

            if (x1 <= x2 + 150  and x1 + 20 >= x2 and y1 <= 480 and y1 - 20 >= 460):
                return True
        return False

    self.canvas.after(50, self.collisionLaserwall(laser, wall))









