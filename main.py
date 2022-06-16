#thaycacac
import turtle
import math
import random
import time
from aasma import agent
import game_easy
import numpy as np
from agents import RandomAgent, GreedyAgent, QLearningAgent
from aasma.utils import compare_results_learning, compare_results

map_easy = [
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "            XXXXXXXXXX                 ",
    "            XP     EXX                 ",
    "            XX X X TXX                 ",
    "            XX X X  XX                 ",
    "            XX X X  TX                 ",
    "            XT   T  HX                 ",
    "            XXXXXXXXXX                 ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       "
]

map_medium = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX XX  XXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXX  XX  XXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXX  XXT XXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXP  XXXBT XXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXX   TXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXX   X XXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXX XXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXX  XXXX XXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXX  XXXXTXX HXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXX  XXXX XX  XXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXX   XXX XX  XXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXX         XXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
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

def run_loop_single(lvl, map, agent, n_evaluations, n_episodes):
    
    results = np.zeros((n_evaluations, n_episodes))

    for evaluation in range(n_evaluations):
        result = run_game(lvl, map, agent, n_episodes)
        results[evaluation] = result


def run_game(lvl, map, agent, n_episodes):
    results = np.zeros(n_episodes)

    for episode in range(n_episodes):
        turtle.clearscreen()
        time.sleep(0.5)
        r = game_easy.init_game(lvl, map, agent, episode)
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

    # Setup agents
    agents = [    
        RandomAgent(),
        GreedyAgent(),
        QLearningAgent()
    ]
   
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
            results = {}
            for agent in agents:
                if self.level == "easy.gif":
                    result = run_game("easy", map_easy, agent, 7)
                    #result = run_loop_single("easy", map_easy, agent, 1, 1)
                    results[agent.name] = result
                elif self.level == "medium.gif":
                    result = run_game("medium", map_medium, agent, 7)
                    #result = run_loop_single("medium", map_medium, agent, 1, 1)
                    results[agent.name] = result
                elif self.level == "hard.gif":
                    result = run_game("hard", map_hard, agent, 7)
                    #result = run_loop_single("hard", map_hard, agent, 1, 1)
                    results[agent.name] = result
                else: #exit
                    turtle.bye()
            # Compare results
            print(results)
            compare_results(results, title="Agents on 'Blindoff' Environment", colors=["blue", "orange", "green"])


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
