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
    "XP  XXXXXXXE         XXXXXXB     XXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXXXX  XX  XXXXXX",
    "X      TXX  XXXXXX  XXXX     XX  XXXXXX",
    "X E    XXX  XX       EXX  XX XX  D  XXX",
    "XXXXXX  XX  XXX              E  XXX  XX",
    "XXXXXX  XX  XXXXXXXAXXXXX     XXXXX  TX",
    "XXXXXX  XX    XXXXX XXXXX        XX  XX",
    "XXXXXX        XXXXX XXXXXXXXXX   XXXXXX",
    "XXXXXX  XXXXXXXXXXX        XXXX  XXXXXX",
    "XXXXXX    XXXXXXXXXXXXXXX  XXXX  XXXXXX",
    "XXXXXX           XXXXXXXX TXXXX    XXXX",
    "XXXXXXXXXXXX     XXXXX TXXXXXXXXX  XXXX",
    "XXXXXXXXXXXXXXX  XXXXX  XXXXXXXXX  XXXX",
    "XXX TXXXXXXXXXX         XXXXXXXXX   TXX",
    "XXXE                    XXXXXXX   EXXXX",
    "XXX        TXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXXXXB     XXXXXX",
    "XXXXXXXXXXE             XXXXX     XXXXX",
    "XXE  XXXXX             EXXXXXXXX  XXXXX",
    "XX   XXXXXXXXXXXXX  XXXXXXXXXXXX EXXXXX",
    "XX    XXXXXXXXXXXX  X     BXXXXX  D XXX",
    "XX     E   XXXXB       XX     XXXXX XXX",
    "XXXXT      D       TXXXXXXXX  XXXXX XXX",
    "XXXXXXXXXXXXXXXX       TXXXX    ED  HXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

map_hard = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP     XT   X     X    XT       XT    X",
    "X X XX     EX XXX X XX         EX XXXXX",
    "X X XXXXXXX X XXX X  X XXXXXXXX      EX",
    "X XXXE    X X   X XX X X        XXXXX X",
    "X X   XXX X XXX X    X XXXXXXXX X     X",
    "X X XXXXX X     XXXXXX  X       X XXXXX",
    "X X XE TX XXXXXXX       X XXXXXXX X   X",
    "X X X X X       X XXX XXX       X X X X",
    "X X X X XXXXXXX X XXX XXXXXXXXX X X X X",
    "X X X X XXXXXXX X XXX XXXXXXXXX X X X X",
    "X                                     X", #passadeira
    "                                       ", 
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "X                                     X", #passadeira
    "X XXXTXXX XXXX XXXXXXXXX X  TXXXX X X X",
    "X XXXXXXX XXXX XXXXXXXXXXXXXXX    X X X",
    "X XXXXXXX XXXX XXXXXXX       X XXXX X X",
    "X X     X XXXX XXXXXXX X X X X        X",
    "X X XXX X XT   XXXXXXX X T X XXXXXXXX X",
    "X   XXX   XXXX        EXXXXX         HX",
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
