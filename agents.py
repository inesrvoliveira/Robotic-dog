import turtle
import math
import random
import main
import time
from aasma import Agent
import numpy as np
from scipy.spatial.distance import cityblock
from collections import defaultdict

N_ACTIONS = 5

DOWN, LEFT, UP, RIGHT, STAY = range(N_ACTIONS)
class RandomAgent(Agent):

    def __init__(self):
        super(RandomAgent, self).__init__("Random Agent")
        self.n_actions = N_ACTIONS

    def action(self, x, y, walls_pos, roads_pos, people_pos,sides_pos, crossroads_pos, sem) -> int:
        return np.random.randint(self.n_actions)

    def next(self, observation, action, next_observation, reward, terminal, info):
        # Not a learning agent
        pass

class GreedyAgent(Agent):

    """
    A baseline agent for the maze environment.
    The greedy agent finds the nearest treasure and moves towards it.
    """

    def __init__(self):
        super(GreedyAgent, self).__init__(f"Greedy Agent")
        self.n_actions = N_ACTIONS
    
    def can_cross(self, d, sides_pos, crossroads_pos,sem, agent_position):
        #------ is he crossing already------------
        if(agent_position in crossroads_pos):
            #print("he is CROSSING!!!!!!!!!!!!!!!!")
            if d == RIGHT:
                return DOWN
            if d == LEFT:
                return UP
            else:
                return d
        #------ does he want to cross ------------
        if(tuple(agent_position) in sides_pos and sem == 0):
            #print("he wants CROSSING!!!!!!!!!!!!!!!!")
            return STAY
        return d

    def find_way(self,can_move,  seq):
        aux = 0
        while True:
            aux = random.choice(seq)
            if(can_move[aux]):
                return aux

    def theres_wall_road(self, d, agent_position, walls_pos, roads_pos,people_pos):
        d_down = (agent_position[0], agent_position[1]-24)
        d_left = (agent_position[0]-24, agent_position[1])
        d_right = (agent_position[0]+24, agent_position[1])
        d_up = (agent_position[0], agent_position[1]+24)
        
        surroundings = [d_down,d_left,d_up,d_right]
        can_move = []
        for i in range(len(surroundings)):
            if(surroundings[i] in walls_pos or surroundings[i] in roads_pos or surroundings[i] in people_pos):
                can_move.append(False)
            else:
                can_move.append(True)
        #for STAY action
        can_move.append(True)

        if(can_move[d]):
            #print("devolvi aqui!!!!!!!!!!")
            #print(can_move)
            return d
        else:
            #choose the preference way if there's a wall
            if(d == DOWN):
                #print("devolvi aqui2222222222!!!!!!!!!!")
                #print(can_move)
                #if(can_move[RIGHT]): return RIGHT
                #if(can_move[LEFT]): return LEFT
                #if(can_move[UP]): return UP
                return self.find_way(can_move, [RIGHT, LEFT, UP, STAY])
            
            if(d == RIGHT):
                #if(can_move[DOWN]): return DOWN
                #if(can_move[LEFT]): return LEFT
                #if(can_move[UP]): return UP
                return self.find_way(can_move, [DOWN, LEFT, UP, STAY])
            
            if(d == LEFT):
                #if(can_move[UP]): return UP
                #if(can_move[DOWN]): return DOWN
                #if(can_move[RIGHT]): return RIGHT
                return self.find_way(can_move, [RIGHT, DOWN, UP, STAY])
            
            if(d == UP):
                #if(can_move[LEFT]): return LEFT
                #if(can_move[RIGHT]): return RIGHT
                #if(can_move[DOWN]): return DOWN
                return self.find_way(can_move, [RIGHT, DOWN, LEFT, STAY])


    def action(self,x,y, walls_pos, roads_pos, people_pos, sides_pos, crossroads_pos, sem) -> int:
        treasure_positions = self.observation
        #print("treasure positions:-------------------------------")
        #print(treasure_positions)

        agent_position = [x,y]
        #print("agent:-------------------------------")
        #print(agent_position)

        closest_treasure = self.closest_treasure(agent_position, treasure_positions)
        #print("closest_treasure:-------------------------------")
        #print(closest_treasure)

        treasure_found = closest_treasure is not None

        if treasure_found:
            #print("direction_to_go:-------------------------------")
            #print(self.direction_to_go(agent_position, closest_treasure))
            d = self.direction_to_go(agent_position, closest_treasure)
            #print("checke walls:-------------------------------")
            d = self.theres_wall_road(d, agent_position, walls_pos,roads_pos,people_pos)

            d = self.can_cross(d, sides_pos, crossroads_pos, sem, agent_position)

            #print(d)
            return d
        else:
            return random.randrange(N_ACTIONS)

    def next(self, observation, action, next_observation, reward, terminal, info):
        # Not a learning agent
        pass

    # ################# #
    # Auxiliary Methods #
    # ################# #

    def direction_to_go(self, agent_position, prey_position):
        """
        Given the position of the agent and the position of a prey,
        returns the action to take in order to close the distance
        """
        distances = np.array(prey_position) - np.array(agent_position)
        abs_distances = np.absolute(distances)
        if abs_distances[0] > abs_distances[1]:
            return self._close_horizontally(distances)
        elif abs_distances[0] < abs_distances[1]:
            return self._close_vertically(distances)
        else:
            roll = random.uniform(0, 1)
            return self._close_horizontally(distances) if roll > 0.5 else self._close_vertically(distances)

    def closest_treasure(self, agent_position, prey_positions):
        """
        Given the positions of an agent and a sequence of positions of all prey,
        returns the positions of the closest prey
        """
        min = math.inf
        closest_prey_position = None
        for p in prey_positions:
            distance = cityblock(agent_position, p)
            if distance < min:
                min = distance
                closest_prey_position = p
        return closest_prey_position

    # ############### #
    # Private Methods #
    # ############### #

    def _close_horizontally(self, distances):
        if distances[0] > 0:
            return RIGHT
        elif distances[0] < 0:
            return LEFT
        else:
            return STAY

    def _close_vertically(self, distances):
        if distances[1] > 0:
            return UP
        elif distances[1] < 0:
            return DOWN
        else:
            return STAY

class QLearningAgent(Agent):

    def __init__(self, learning_rate = 0.3, discount_factor = 0.99, exploration_rate = 1, initial_q_values = 0):
        self._Q = defaultdict(lambda: np.ones(N_ACTIONS) * initial_q_values)
        self._learning_rate = learning_rate
        self._discount_factor = discount_factor
        self._exploration_rate = exploration_rate
        self.n_actions = N_ACTIONS
        super(QLearningAgent, self).__init__("Q-Learning")

    def can_cross(self, actions, sides_pos, crossroads_pos, sem, agent_position):
        #------ does he want to cross ------------
        if(tuple(agent_position) in sides_pos and sem == 0):
            #print("he wants CROSSING!!!!!!!!!!!!!!!!")
            return [STAY]
        return actions
    
    def action(self, x, y, walls_pos, roads_pos, people_pos,sides_pos, crossroads_pos, sem, exploration = True) -> int:
        d = 0
        agent_position = [x, y]
        position = tuple(agent_position)
        #Access Q-Values for current observation
        q_values = self._Q[position]

        if not self.training or (self.training and np.random.uniform(0, 1) > self._exploration_rate):
            # Exploit
            actions = np.argwhere(q_values == np.max(q_values)).reshape(-1)
            # print("checke walls:-------------------------------")
            #actions = self.theres_wall(actions, agent_position, walls_pos)
        else:
            # Explore
            actions = range(self.n_actions)
            # print("checke walls:-------------------------------")
            #actions = self.theres_wall(actions, agent_position, walls_pos)

        actions = self.can_cross(actions, sides_pos, crossroads_pos, sem, agent_position)

        return np.random.choice(actions)

    def next(self, observation, action, next_observation, reward, terminal):

        x, a, r, y = tuple(observation), action, reward, tuple(next_observation)
        alpha, gamma = self._learning_rate, self._discount_factor

        Q_xa = self._Q[x][a]
        Q_y = self._Q[y]

        max_Q_ya = max(Q_y)

        # Update rule for Q-Learning
        self._Q[x][a] = Q_xa + alpha * (r + gamma * max_Q_ya - Q_xa)