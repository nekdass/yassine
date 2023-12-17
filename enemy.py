from PIL import Image, ImageTk
import tkinter as tk
from player import Player
import random as rd
class Enemy:

    def __init__(self, canvas):
        self.canvas = canvas
        self.enemies = []
        self.rows = 2
        self.columns = 10


        self.speed = 0.3
        self.direction = 1

        self.image = tk.PhotoImage(file="enemy1_1.png").subsample(4, 4)

        self.createEnemies()
        self.enemyLaser()


    def createEnemies(self):
        y = 40
        for i in range(self.columns):
            for j in range(self.rows):
                x = i * 50
                y = j * 50
                enemyHitbox = self.canvas.create_rectangle(x + 30, y, x + 60, y + 30, fill="red", outline="")
                enemy = self.canvas.create_image(x + 45, y + 15, anchor=tk.CENTER, image=self.image)
                self.enemies.append({"hitBox": enemyHitbox, "imageId": enemy, "x": x, "y": y})

            self.moveGroup()







    def moveGroup(self):
        y = 20
        for enemy in self.enemies:
            self.canvas.move(enemy["hitBox"], self.speed * self.direction, 0)
            self.canvas.move(enemy["imageId"], self.speed * self.direction, 0)
            enemy["x"] += self.speed * self.direction

        if self.enemies[0]["x"] <= 0:
            self.direction *= -1
            for enemy in self.enemies:
                self.canvas.move(enemy["hitBox"], 0, y)
                self.canvas.move(enemy["imageId"], 0, y)
                enemy["y"] += y
        elif self.enemies[-1]["x"] + 30 >= 740:
            self.direction *= -1

        self.canvas.after(50, self.moveGroup)


    def enemyLaser(self):
        col = rd.randint(0, self.columns)
        enemyPosition = self.enemies[col]["x"], self.enemies[col]["y"]
        shot = self.canvas.create_rectangle(enemyPosition[0], enemyPosition[1] + 30, enemyPosition[0] + 10, enemyPosition[1] + 50, fill="green", outline="")
        self.moveEnemylaser(shot)
        self.canvas.move(shot, 10, 0)
        self.canvas.after(5000, self.enemyLaser)

    def moveEnemylaser(self, shot):
        self.canvas.move(shot, 0, 10)
        self.canvas.after(50, self.moveEnemylaser, shot)