class Wall:

    def __init__(self, canvas):

        self.canvas = canvas
        self.walls = []
        self.createWalls()
        self.wallLives = [3, 3, 3]

    def createWalls(self):
        x = -200
        for i in range(3):
            x += 250
            wall = self.canvas.create_rectangle(x, 480,x + 150, 460, fill="orange")


