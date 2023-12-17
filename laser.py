class LaserP:
    def __init__(self, canvas, playerCoords):

        self.canvas = canvas
        self.playerCoords = playerCoords


    def shootLaser(self, event):
        x1 = self.playerCoords[0]
        y1 = self.playerCoords[1]


        laserId = self.canvas.create_rectangle(x1 - 20, y1 + 10, x1 + 20, y1 - 20, fill="yellow")
        self.moveLaser(laserId)

    def moveLaser(self, laserId):
        self.canvas.move(laserId, 0, -10)
#        if self.checkCollision(laserId):
#            self.canvas.delete(laserId)
#        else:
        self.canvas.after(50, self.moveLaser, laserId)

