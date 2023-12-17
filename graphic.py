from PIL import Image, ImageTk
import tkinter as tk
from player import Player
from enemy import Enemy
from wall import Wall
from laser import LaserP
class Graphics:
    def __init__(self, mw):
        self.mw = mw
        self.mw.title('Space invaders')
        self.mw.geometry('900x600')
        self.createWidget(mw)

        self.player = Player(self.canvas)
        self.enemy = Enemy(self.canvas)
        self.wall = Wall(self.canvas)

        self.playerCoords = self.player.playerCoords()
        self.laser = LaserP(self.canvas, self.playerCoords)

        self.mw.bind('<Left>', self.player.moveLeft)
        self.mw.bind('<Right>', self.player.moveRight)

        self.mw.bind('<space>', self.laser.shootLaser)

    def createWidget(self, mw):

        self.canvas = tk.Canvas(self.mw,background='black', height=600, width=900)
        self.canvas.pack(side='bottom', anchor='nw')
        self.img = ImageTk.PhotoImage(file="background.jpg")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

        self.quitButton = tk.Button(self.mw,
                                    text='Quit',
                                    command=self.mw.destroy,
                                    bg='black',
                                    fg='white',
                                    bd=0,
                                    relief='flat',
                                    font=("Helvetica", 12) )

        self.quitButton.place(x=830, y=400)

"""     self.startButton = tk.Button(self.master, text='Start', command='h', bg='black', fg='white',height=1, width=5) 

        self.score = tk.StringVar(self.mw, 'Score :')
        self.label = tk.Label(self.mw, textvariable=self.score)
        self.label.place(x=50, y=15)


        self.lives = tk.StringVar(self.mw, 'Lives :')
        self.labelVie = tk.Label(self.mw, textvariable=self.lives)
        self.labelVie.place(x=500, y=15)
        
        def gameOver(self):
        self.canvas.create_text(300, 200, text="Game Over", font=("Helvetica", 30), fill="red")
"""


