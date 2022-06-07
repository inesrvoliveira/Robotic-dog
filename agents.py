import turtle
import math
import random
import main
import time

class RandomAgent(turtle.Turtle):
            def __init__(self):
                turtle.Turtle.__init__(self)
                self.actions_size = 4
                self.penup()
                self.goto(2000, 2000)
                self.hideturtle()
            
            def get_action(self):
                return random.choice(range(self.actions_size))

            def make_action(self, player):
                action = self.get_action()
                if(action == 0):
                    player.up()
                if(action == 1):
                    player.down()
                if(action == 2):
                    player.right()
                if(action == 3):
                    player.left()

class SmartAgent(turtle.Turtle):
            def __init__(self):
                turtle.Turtle.__init__(self)
                self.actions_size = 4
                self.penup()
                self.goto(2000, 2000)
                self.hideturtle()
            
            def get_action(self, player):

                return 

            def make_action(self, player):
                action = self.get_action()
                if(action == 0):
                    player.up()
                if(action == 1):
                    player.down()
                if(action == 2):
                    player.right()
                if(action == 3):
                    player.left()