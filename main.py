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
    "            XUUUUUUEXX                 ",
    "            XXUXUXUUXX                 ",
    "            XXUXUXUUXX                 ",
    "            XXUXUXUUUX                 ",
    "            XUUUUUUUUX                 ",
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
    "                                       ",
    "                                       ",
    "          XXXXXXXXXXXXXXX              ",
    "          XXXXEUU XXXXXXX              ",
    "          XXXX XXUUXXXXXX              ",
    "          XXX UXXUUXXXXXX              ",
    "          XXXEUUUUUBDUUXX              ",
    "          XXXUXXXUUUXXXXX              ",
    "          XXXUXXXUXUXXXXX              ",
    "          XXXUXXXU UXXXXX              ",
    "          XXXUXXX XUXXXXX              ",
    "          XXXUUEU X XXXXX              ",
    "          XXXUUUUUU XXXXX              ",
    "          XXXUU XXXEXXXXX              ",
    "          XXXUUXXXXUXXXXX              ",
    "          XXXUUXXXXUXXXXX              ",
    "          XXXUUUXXXUXXXXX              ",
    "          XXXXXUUUUBDUUXX              ",
    "          XXXXXXXXXXXXXXX              ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       ",
    "                                       "
]

map_hard = [
    "                                       ",
    "                                       ",
    "         XXXXXXXXXXXXXXXXXXXX          ",
    "         XXXXXXXXXXXXXXXXXXXX          ",
    "         X    X   X   E X   X          ",
    "         X X    X E X     X X          ",
    "         XXXXXXXXXXXXXXX XXXX          ",
    "         XXXXXXXXUUUU    XXXX          ",
    "         XXXXXXXXUUXXXXXXXXXX          ",
    "         XXXXXXXXUUXXXXXXXXXX          ",
    "         XXXXXXSXZZXXXXXXXXXX         ", #passadeira
    "         KKKKKKKKYYKKKKKKKKKKC         ", 
    "         RRRRRRRRYYRRRRRRRRRRV         ",
    "         RRRRRRRRYYRRRRRRRRRRC         ",
    "         RRRRRRRRYYRRRRRRRRRRO         ",
    "         RRRRRRRRYYRRRRRRRRRRG         ",
    "         RRRRRRRRYYRRRRRRRRRRO         ",
    "         XXXXXXXXZZXSXXXXXXXX          ", #passadeira
    "         XXXXXXXXUUXXXXXXXXXX          ",
    "         XXXXUUUUUUUUUUU UUUX          ",
    "         XXXXU X X XXUXUUUXUX          ",
    "         XXXXUUEUUUUUUUUXUUUX          ",
    "         XXXXXXXXXXXXXXXXXXXX          "
]

def run_loop_single(lvl, map, agent, n_evaluations, n_episodes):
    
    results = np.zeros((n_evaluations, n_episodes))

    for evaluation in range(n_evaluations):
        result = run_game(lvl, map, agent, n_episodes)
        results[evaluation] = result
    return results,result


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
            results1 = {}
            for agent in agents:
                if self.level == "easy.gif":
                    #result = run_game("easy", map_easy, agent, 3)
                    result, result1 = run_loop_single("easy", map_easy, agent, 10, 10)
                    results[agent.name] = result
                    results1[agent.name] = result1
                elif self.level == "medium.gif":
                    #result = run_game("medium", map_medium, agent, 3)
                    result, result1 = run_loop_single("medium", map_medium, agent, 10, 10)
                    results[agent.name] = result
                    results1[agent.name] = result1
                elif self.level == "hard.gif":
                    #result = run_game("hard", map_hard, agent, 3)
                    result, result1 = run_loop_single("hard", map_hard, agent, 10, 10)
                    results[agent.name] = result
                    results1[agent.name] = result1
                else: #exit
                    turtle.bye()
            # Compare results
            print(results)
            compare_results(results1, title="Agents on 'Blindoff' Environment", colors=["blue", "orange", "green"])
            compare_results_learning(results, title="Agents on 'Blindoff' Environment", colors=["blue", "orange", "green"])


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
