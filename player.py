from PIL import Image, ImageTk
import tkinter as tk


class Player:

    def __init__(self, canvas):
        self.canvas = canvas

        self.image = tk.PhotoImage(file="ship.png")
        self.id = canvas.create_image(275, 510, anchor=tk.NW, image=self.image)
        x1, y1 = canvas.coords(self.id)
        self.hitBox = canvas.create_rectangle(x1, y1, x1 +50, y1 - 5, fill="", outline="")

    def moveLeft(self, event):
        position = self.canvas.coords(self.id)
        if position[0] > 0:
            self.canvas.move(self.id, -20, 0)
            self.canvas.move(self.hitBox, -20, 0)

    def moveRight(self, event):
        position = self.canvas.coords(self.id)
        if position[0] < 740:
            self.canvas.move(self.id, 20, 0)
            self.canvas.move(self.hitBox, 20, 0)

    def playerCoords(self):
        return self.canvas.coords(self.id)

    canvas.after(50, playerCoords)