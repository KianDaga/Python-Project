from tkinter import X

import tkinter as tk
from Shape import Shape
from Text import Text
import turtle
import time
import random
class Game:
    def __init__(self):
        self.win = turtle.Screen()
        self.win.bgcolor("white")
        self.win.title("Catch The Circles!")
        self.win.tracer(0)
        self.shapes = []
        self.score = 0
        self.start_time = time.time()
        self.duration = 20
        self.score_text  = Text(-200,250, f"score: {self.score}")
        self.timer_text = Text(200,250, f"time: {self.duration}")

    def create_shapes(self):
        x = random.randint(-250,250)
        y = 250
        shape_list = ["circle", "square", "triangle"]
        color_list = ["red", "blue", "green", "yellow", "purple", "orange"]
        shape = random.choice(shape_list)
        color = random.choice(color_list)
        new_shape = Shape(x, y, shape, color)
        new_shape.show()
        self.shapes.append(new_shape)
    def move_shapes(self):
        for s in self.shapes.copy():
            s.move()
            if s.shape.ycor() < -250:
                self.shapes.remove(s)
                s.hide() 
    def on_shape_click(self,x,y):
        for s in self.shapes.copy():
            if s.shape.distance(x,y) < 40 and s.shape.shape() == "circle":
                self.shapes.remove(s)
                s.hide()
                self.score += 1
            elif s.shape.distance(x,y) < 40 and s.shape.shape() != "circle":
                self.shapes.remove(s)
                s.hide()
                self.score -= 1

    def update_timer(self):
        time_past = time.time() - self.start_time
        time_past = int(time_past)
        time_left = self.duration - time_past
        time_left = int(time_left)
        time_left = max(time_left,0)
        self.timer_text.writetext(f"Time: {time_left}")
        self.score_text.writetext(f"Score: {self.score}")
        if time_left > 0:
            return(True)
        else:
            return(False)
    
    def start(self):
        self.win.listen()
        self.win.onclick(self.on_shape_click)
        while self.update_timer() == True:
            self.win.update()
            self.create_shapes()
            self.move_shapes()
            time.sleep(0.1)
        self.win.textinput("Game Over!", f"Your highest score is: {self.score}")
