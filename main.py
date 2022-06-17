
import turtle
import math
import random
import time
from aasma import agent
import game_easy
import numpy as np
from agents import RandomAgent, GreedyAgent, QLearningAgent
from aasma.utils import compare_results_learning, compare_results

#number of episodes
n_epi = 10

#number of evaluations
n_eval = 10

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
    "         XXXXXXSXZZXXXXXXXXXX          ", #passadeira
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
    
    results_steps = np.zeros((n_evaluations, n_episodes))
    results_time = np.zeros((n_evaluations, n_episodes))
    results_score = np.zeros((n_evaluations, n_episodes))

    for evaluation in range(n_evaluations):
        result_steps, result_time, result_score = run_game(lvl, map, agent, n_episodes)
        results_steps[evaluation] = result_steps
        results_time[evaluation] = result_time
        results_score[evaluation] = result_score
    return results_steps, result_steps, results_time, result_time, results_score, result_score


def run_game(lvl, map, agent, n_episodes):

    results_steps = np.zeros(n_episodes)
    results_time = np.zeros(n_episodes)
    results_score = np.zeros(n_episodes)
    
    for episode in range(n_episodes):
        turtle.clearscreen()
        time.sleep(0.5)
        results_steps[episode], results_time[episode], results_score[episode] = game_easy.init_game(lvl, map, agent, episode)
                
    print("-------------------------results:--------------------------")
    print(results_steps)
    print(results_time)
    print(results_score)
    return results_steps,results_time, results_score


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
            results_steps_episode = {}
            results_steps_evaluation = {}
            results_time_episode = {}
            results_time_evaluation = {}
            results_score_episode = {}
            results_score_evaluation = {}
            for agent in agents:
                if self.level == "easy.gif":
                    #result = run_game("easy", map_easy, agent, 3)
                    results_steps, result_steps, results_time, result_time, results_score, result_score = run_loop_single("easy", map_easy, agent, n_eval, n_epi)
                    results_steps_evaluation[agent.name] = results_steps
                    results_steps_episode[agent.name] = result_steps
                    results_time_evaluation[agent.name] = results_time
                    results_time_episode[agent.name] = result_time
                    results_score_evaluation[agent.name] = results_score
                    results_score_episode[agent.name] = result_score
                elif self.level == "medium.gif":
                    #result = run_game("medium", map_medium, agent, 3)
                    results_steps, result_steps, results_time, result_time, results_score, result_score = run_loop_single("medium", map_medium, agent, n_eval, n_epi)
                    results_steps_evaluation[agent.name] = results_steps
                    results_steps_episode[agent.name] = result_steps
                    results_time_evaluation[agent.name] = results_time
                    results_time_episode[agent.name] = result_time
                    results_score_evaluation[agent.name] = results_score
                    results_score_episode[agent.name] = result_score
                elif self.level == "hard.gif":
                    #result = run_game("hard", map_hard, agent, 3)
                    results_steps, result_steps, results_time, result_time, results_score, result_score = run_loop_single("hard", map_hard, agent, n_eval, n_epi)
                    results_steps_evaluation[agent.name] = results_steps
                    results_steps_episode[agent.name] = result_steps
                    results_time_evaluation[agent.name] = results_time
                    results_time_episode[agent.name] = result_time
                    results_score_evaluation[agent.name] = results_score
                    results_score_episode[agent.name] = result_score
                else: #exit
                    turtle.bye()

            # Compare results
            parameter = 0 # 0 - steps, 1 - time, 2 - score

            # steps
            parameter = 0
            compare_results(results_steps_episode, parameter, title="Agents on 'Blindoff' Environment", colors=["blue", "orange", "green"])
            compare_results_learning(results_steps_evaluation, parameter, title="Agents on 'Blindoff' Environment", colors=["blue", "orange", "green"])

            # time
            parameter = 1
            compare_results(results_time_episode, parameter, title="Agents on 'Blindoff' Environment", colors=["blue", "orange", "green"])
            compare_results_learning(results_time_evaluation, parameter, title="Agents on 'Blindoff' Environment", colors=["blue", "orange", "green"])

            # score
            parameter = 2
            compare_results(results_score_episode, parameter, title="Agents on 'Blindoff' Environment", colors=["blue", "orange", "green"])
            compare_results_learning(results_score_evaluation, parameter, title="Agents on 'Blindoff' Environment", colors=["blue", "orange", "green"])


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
    time.sleep(1)


main()
