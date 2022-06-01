#thaycacac
import turtle
import math
import random
import time
import game_easy

map_easy = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXXE         XXXXXX      XXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXXXX  XX  XXXXXX",
    "X       XX  XXXXXX  XXXX     XX    XXXX",
    "X       XX  XXXXXX           XX    XXXX",
    "XXXXXX  XX  XXXXXX              XXXXXXX",
    "XXXXXX  XX  XXXXXXXXXXXXX     XXXXXXXXX",
    "XXXXXX  XX    XXXXXXXXXXX        XXXXXX",
    "XXXXXX        XXXXXXXXXXXXXXXX   XXXXXX",
    "XXXXXX  XXXXXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "X         XXXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "XE               XXXXXXXXXXXXXX    XXXX",
    "XXXXXXXXXXXX     XXXXX  XXXXXXXXX  XXXX",
    "XXXXXXXXXXXXXXX  XXXXX  XXXXXXXXX  XXXX",
    "XXX  XXXXXXXXXX         XXXXXXXXX    XX",
    "XXX                     XXXXXXX    XXXX",
    "XXX        TXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXXXX      XXXXXX",
    "XXXXXXXXXXE             XXXXX     XXXXX",
    "XXXXXXXXXX              XXXXXXXX  XXXXX",
    "XXXXXXXXXXXXXXX     XXXXXXXXXXXX  XXXXX",
    "XXXXXXXXXXXXXXX     X      XXXXX    XXX",
    "XXXXXXXXXXXXXXXT       XX     XXXX  XXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX  XXXX  XXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX        HXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

map_medium = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXXE         XXXXXX      XXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXXXX  XX  XXXXXX",
    "X      TXX  XXXXXX  XXXX     XX   TXXXX",
    "X E    XX  XXX       EXX  XX XX     XXX",
    "XXXXXX  XX  XXX              E  XXX  XX",
    "XXXXXX  XX  XXXXXX  XXXXX     XXXXX   X",
    "XXXXXX  XX    XXXX  XXXXX        XX  XX",
    "X  XXX        XXXX  XXXXXXXXXX   XXXXXX",
    "X  XXX  XXXXXXXXX   E      XXXX  XXXXXX",
    "X         XXXXXXXXXXXXXXX  XXXX  XXXXXX",
    "XE               XXXXXXXX  XXXX    XXXX",
    "XXXXXXXXXXXX     XXXXX TX    XXXX  XXXX",
    "XXXXXXXXXXXXXXX  XXXXX  XXX  XXXX  XXXX",
    "XXX TXXXXXXXXXX         XXX  XXXX   TXX",
    "XXXE                    XXXXXXX   EXXXX",
    "XXX        TXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXXXX      XXXXXX",
    "XXXXXXXXXXE             XXXXX     XXXXX",
    "XXE  XXXXX             EXXXXXXXX  XXXXX",
    "XX   XXXXXXXXXXXXX  XXXXXXXXXXXX EXXXXX",
    "XX    XXXXXXXXXXXX  X      XXXXX    XXX",
    "XX     E   XXXX        XX     XXXX  XXX",
    "XXXXT              TXXXXXXXX  XXXX  XXX",
    "XXXXXXXXXXXXXXXX       TXXXX    E   HXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

map_hard = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP     XT   X     X X  XT       XT    X",
    "X X XX     EX X X X XX         EX XXXXX",
    "X X XXXXXXX X XXX X  X XXXXXXXX X    EX",
    "X XXXE    X X   X XX X X        XXXXX X",
    "X X   X X X XXX X    X XXXXXXXX X     X",
    "X X XXXXX X     XXXXXX  X       X XXXXX",
    "X X XE TX XXXXXXX       X XXXXXXX X   X",
    "X X X X X       X X X XXX       X X X X",
    "X X X X XXXXXXX X X X XXXXXXXXX X X X X",
    "X X X X X   X X X X X X         X X X X",
    "X X X X       X   X   X XXXXX XXX   X X",
    "X X X XXXXXXXXXXXXX XXX X X XXX XXXXX X",
    "XT  X    X             EX             X",
    "XXXXXXXX X XXXXXXXXXT   X X X XXXXX XXX",
    "X        X         XXXXXXXX XXXT  XXX X",
    "XXXXXXXX X XXXXXXX X     EXE          X",
    "X        X       X X X XX XXXXXXXXXXX X",
    "X X XXX XXXXXXXX X X X X          X X X",
    "X X XTX X      X X X X X X  TXXXX X X X",
    "X X    EX X XX X X X XXXXXXXXX    X X X",
    "X XXXXXXX X X  X XXX X       X XXXX X X",
    "X X     X XXXX X     X X X X X        X",
    "X X X X X XT   XXXXXXX X T X XXXXXXXX X",
    "X   X X   XXXX        EXXXXX         HX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]


def main():
    screen = turtle.Screen()
    screen.tracer(0)

    easy = "easy.gif"
    medium = "medium.gif"
    hard = "hard.gif"
    exit = "exit.gif"
    screen.addshape(easy)
    screen.addshape(medium)
    screen.addshape(hard)
    screen.addshape(exit)

    # create level
    class Level(turtle.Turtle):

        level = ""

        def __init__(self, level, position_y):
            turtle.Turtle.__init__(self)
            self.shape(level)
            self.penup()
            self.goto(0, position_y)
            self.level = level
            self.onclick(self.play_game)

        def play_game(self, x, y):
            if self.level == "easy.gif":
                turtle.clearscreen()
                game_easy.init_game("easy", map_easy)
            elif self.level == "medium.gif":
                turtle.clearscreen()
                game_easy.init_game("medium", map_medium)
            elif self.level == "hard.gif":
                turtle.clearscreen()
                game_easy.init_game("hard", map_hard)
            else: #exit
                turtle.bye()


    # add level
    level_easy = Level(easy, 20)
    level_medium = Level(medium, -50)
    level_hard = Level(hard, -120)
    level_exit = Level(exit, -190)

    screen.bgpic("menu.png")
    screen.title("Blindoff")
    screen.setup(1024, 740)
    screen.tracer(0)

    #screen.listen()
    time.sleep(3)


main()
