#thaycacac
import turtle
import math
import random
import time
import game_easy
import numpy as np

map_easy = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXXXE         XXXXX       XXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXXX   XX  XXXXXX",
    "X       XX  XXXXXX  XXXXXX   XX    XXXX",
    "X       XX  XXXXXX           XX    XXXX",
    "XXXXXX  XX  XXXXXX              XXXXXXX",
    "XXXXXX  XX  XXXXXXXXXXXXX     XXXXXXXXX",
    "XXXXXX  XX  XXXXXXXXXXXXX        XXXXXX",
    "XXXXXX  XX  XXXXXXXXXXXXXXXXXX   XXXXXX",
    "XXXXXX  XXXXXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "X         XXXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "XE               XXXXXXXXXXXXXX    XXXX",
    "XXXXXXXXXXXX     XXXXXXXXXXXXXXXX  XXXX",
    "XXXXXXXXXXXXX    XXXXXXXXXXXXXXXX  XXXX",
    "XXXXXXXXXXXXX         XXXXXXXXXXX    XX",
    "XXX                  TXXXXXXXXX    XXXX",
    "XXX                   XXXXXXXXX  XXXXXX",
    "XXXXXXXXXX            XXXXX      XXXXXX",
    "XXXXXXXXXXE             XXXXX     XXXXX",
    "XXXXXXXXXX              XXXXXXXX  XXXXX",
    "XXXXXXXXXXXXXXX        XXXXXXXXX  XXXXX",
    "XXXXXXXXXXXXXXX            XXXXX    XXX",
    "XXXXXXXXXXXXXXXT              XXXX  XXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX        XXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX        HXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

map_medium = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXXXE     T  TXXXXX       XXXXXX",
    "X  XXXXXXX                       XXXXXX",
    "X      TXX                    TBTXXXXXX",
    "X       XX            E          DT XXX",
    "XXXXXX  XX    TBT               XX  XXX",
    "XXXXXX  XX    XXXAX           XXXX    X",
    "XXXXXX        XXXTX    XX        X    X",
    "XXXXXX        XXXXX   XXXXXX     X    X",
    "XXXXXX        XXXX   XXXXXXX    XX    X",
    "XXXXXX             TXXXXXXXXX    X   XX",
    "XXXXXX           T  XXXXXXXXXX       XX",
    "XXXXXT           XXXXXXXXXXXXX      XXX",
    "XXXXX            XXXXXXXXXXXXXX     XXX",
    "XXX T            XXXXXXXXXXXXXX    TXXX",
    "XXX              XXXXXXXXXXXXXXX   XXXX",
    "XXX             XXXXXXXXXXXXXXX    XXXX",
    "XXXXXXXX        XXXXXXXXXXX         XXX",
    "XXXXXXXX  E             XXXXX       XXX",
    "XX   XXX                XXXXXXXX    XXX",
    "XX   XXX            XXXXXXXXXXXX    XXX",
    "XX    XX                   XXXXX    XXX",
    "XX     E                     BXXXX  XXX",
    "XXXX   T           TXXXXXXXX  XXXX  XXX",
    "XXXXXXXXXXXXXXXX       TXXXX     D  HXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

map_hard = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP     XT   X  T  X     T             X",
    "X X XX      X  XX XT           E  XXXXX",
    "X X XXXXXXX X  XX X  X XXXXXXXX T X  EX",
    "X XXX     X X T X X  X X  X      XX   X",
    "X X   XXX X XXX X  T X XX X     X     X",
    "X X XXXXX X    TXXXXXX  X X     X XXXXX",
    "X X XE TX XXXXXXX       X X     X X   X",
    "X X X X X       X XXX XXX       X X X X",
    "X X X X XXXXXXX X XXX XXXXXX    X X X X",
    "X X X X XXXXXXX X XXX XXXXXX  T X X X X",
    "ZZZZZZZZZZZZZZZZSZZZZZZZZZZZZZZZZZZZZZZ", #passadeira
    "KKKKKKKKKKKKKKKKKYYYKKKKKKKKKKKKKKKKKKKC", 
    "RRRRRRRRRRRRRRRRRYYYRRRRRRRRRRRRRRRRRRRV",
    "RRRRRRRRRRRRRRRRRYYYRRRRRRRRRRRRRRRRRRRC",
    "RRRRRRRRRRRRRRRRRYYYRRRRRRRRRRRRRRRRRRRO",
    "RRRRRRRRRRRRRRRRRYYYRRRRRRRRRRRRRRRRRRRG",
    "RRRRRRRRRRRRRRRRRYYYRRRRRRRRRRRRRRRRRRRO",
    "ZZZZZZZZZZZZZZZZZZZZSZZZZZZZZZZZZZZZZZZ", #passadeira
    "X XXXXXXX XXXX XXXXXXXXXXXXXXXXXXTX X X",
    "X XXXXXXX XXXX XXXXXXXXXXXXXXX    X X X",
    "X XXXXXXX XXXX XXXXXXX       XTXXXX X X",
    "X X     X XXXX XXXXXXX X X X X        X",
    "X X XXX X XT   XXXXXXX X T X XXXXXXXX X",
    "X   XXX   XXXX        EXXXXX         HX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

def run_game(lvl,map, n_episodes):
    results = np.zeros(n_episodes)

    for episode in range(n_episodes):
        turtle.clearscreen()
        time.sleep(0.5)
        r = game_easy.init_game(lvl, map)
        results[episode] = r #steps?
    print("results:--------------------------")
    print(results)
    return results


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
                run_game("easy", map_easy, 3)
            elif self.level == "medium.gif":
                run_game("medium", map_medium, 3)
            elif self.level == "hard.gif":
                run_game("hard", map_hard, 3)
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
    time.sleep(2)


main()
