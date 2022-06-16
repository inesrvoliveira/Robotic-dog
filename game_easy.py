#thaycacac
import turtle
import math
import random
import main
import time
import agents
import copy
import numpy as np

screen = turtle.Screen()

def init_screen():
    screen.bgcolor("black")
    screen.title("Blindoff")
    screen.setup(1000, 750)
    screen.tracer(0)

def init_game(name_level, map_level, agent, n_episode):
    #try:
        init_screen()

        #register shape
        wall_easy = "grass1.gif"
        screen.addshape(wall_easy)
        wall_medium = "grass2.gif"
        screen.addshape(wall_medium)
        wall_hard = "grass3.gif"
        screen.addshape(wall_hard)
        image_bones = "bones.gif"
        screen.addshape(image_bones)
        image_logo = "logo.gif"
        screen.addshape(image_logo)
        left = "dog_left.gif"
        screen.addshape(left)
        right = "dog_right.gif"
        screen.addshape(right)
        top = "dog_top.gif"
        screen.addshape(top)
        bottom = "dog_bottom.gif"
        screen.addshape(bottom)
        image_people = ["people_bottom.gif", "people_right.gif", "people_left.gif", "people_top.gif"]
        for i in range(4):
            screen.addshape(image_people[i])
        image_treasures = ["treasure_0.gif", "treasure_1.gif", "treasure_2.gif", "treasure_3.gif", "treasure_4.gif"]
        for i in range(5):
            screen.addshape(image_treasures[i])
        image_buttons = ["door_button.gif","door_button_activated.gif"]
        for i in range(2):
            screen.addshape(image_buttons[i])
        image_doors = ["closed_door.gif","opened_door.gif", "opened_door2.gif"]
        for i in range(3):
            screen.addshape(image_doors[i])
        image_road = ["road.gif", "road2.gif"]
        for i in range(2):
            screen.addshape(image_road[i])
        
        sideroad = "side_road.gif"
        screen.addshape(sideroad)
        crossroad = "crosswalk.gif"
        screen.addshape(crossroad)
        image_semaphore = ["red.gif", "green.gif"]
        for i in range(2):
            screen.addshape(image_semaphore[i])

        image_cars = ["car1_esq.gif", "car2_esq.gif", "car2_dir.gif", "car1_dir.gif"]
        for i in range(4):
            screen.addshape(image_cars[i])
        
        # create list
        walls = []
        treasures = []
        persons = []
        buttons = []
        doors = []
        buttons_pos = []
        doors_pos = []
        roads = []
        sideroads = []
        crossroads = []
        semaphores = []
        side_pos = []
        cars = []
        available_pos = []

        start = time.time()

        timer = 0

        #show Score
        def show_score(timer, n_steps, hp):
            turtle.clear()
            turtle.color('white')
            turtle.penup()
            turtle.goto(100, 305)
            style = ('Courier', 20, 'bold')
            turtle.write("Ep: {0}   Time: {1}    Steps: {2}    Score: {3}".format(n_episode,timer, n_steps, hp), font=style, align='center')
            turtle.hideturtle()
       
        
        #create logo blindoff
        class LogoBlindoff(turtle.Turtle):

            def __init__(self):
                turtle.Turtle.__init__(self)
                self.shape(image_logo)
                self.penup()
                self.goto(-420, 330)
                self.onclick(self.main)

            def main(self, x, y):
                turtle.clearscreen()
                main.main()
                turtle.done()

        #create pen
        class Pen(turtle.Turtle):
            def __init__(self):
                turtle.Turtle.__init__(self)
                if name_level == "easy":
                    self.shape(wall_easy)
                elif name_level == "medium":
                    self.shape(wall_medium)
                else:
                    self.shape(wall_hard)
                self.penup()
                self.speed(0)

        def is_edge_space(move_to_x, move_to_y):
            return (move_to_x, move_to_y) == (-480,24) or (move_to_x, move_to_y) == (-480,-144) or (move_to_x, move_to_y) == (480,-144) or (move_to_x, move_to_y) == (480,24)

        def can_move(move_to_x, move_to_y, player, isPerson):
            if (move_to_x, move_to_y) not in walls and (move_to_x, move_to_y) not in doors_pos and not is_edge_space(move_to_x, move_to_y) :
                if isPerson:
                    if (move_to_x, move_to_y) not in side_pos:
                        player.goto(move_to_x, move_to_y)
                        return True  
                    else:
                        return False
                else:
                    player.goto(move_to_x, move_to_y)
                    return True
            elif (move_to_x, move_to_y) in doors_pos:
                i = doors_pos.index((move_to_x, move_to_y))
                if not doors[i].is_closed:
                    player.goto(move_to_x, move_to_y)
                    return True
                else:
                    return False
            else:
                return False

        #create player
        class Player(turtle.Turtle):
            
            def __init__(self):
                turtle.Turtle.__init__(self)
                self.shape(bottom)
                self.penup()
                self.speed(0)
                self.hp = 500
                self.n_steps = 0
                #show_score(timer, self.n_steps, self.hp)

            def up(self):
                self.shape(top)
                move_to_x = self.xcor()
                move_to_y = self.ycor() + 24
                can_move(move_to_x, move_to_y, self, False)
                self.n_steps += 1
                #show_score(timer, self.n_steps, self.hp)

            def down(self):
                self.shape(bottom)
                move_to_x = self.xcor()
                move_to_y = self.ycor() - 24
                can_move(move_to_x, move_to_y, self, False)
                self.n_steps += 1
                #show_score(timer, self.n_steps, self.hp)
                
            def left(self):
                self.shape(left)
                move_to_x = self.xcor() - 24
                move_to_y = self.ycor()
                can_move(move_to_x, move_to_y, self, False)
                self.n_steps += 1
                #show_score(timer, self.n_steps, self.hp)
                
            def right(self):
                self.shape(right)
                move_to_x = self.xcor() + 24
                move_to_y = self.ycor()
                can_move(move_to_x, move_to_y, self, False)
                self.n_steps += 1
                #show_score(timer, self.n_steps, self.hp)

            def is_collision(self, other):
                a = self.xcor() - other.xcor()
                b = self.ycor() - other.ycor()
                distance = math.sqrt((a ** 2) + (b ** 2))
                if distance < 5:
                    return True
                else:
                    return False

        #create treasure
        class Treasure(turtle.Turtle):
            
            def __init__(self, x, y):
                turtle.Turtle.__init__(self)
                if name_level == "easy":
                    self.number_random = random.randint(0, 1)
                elif name_level == "medium":
                    self.number_random = random.randint(0, 2)
                else:
                    self.number_random = random.randint(3, 4)
                self.shape(image_treasures[self.number_random])
                self.hp = (self.number_random + 1) * 100
                self.penup()
                self.speed(0)
                self.goto(x, y)

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        #create bones
        class Bones(turtle.Turtle):
            
            def __init__(self):
                turtle.Turtle.__init__(self)
                self.shape(image_bones)
                self.penup()
                self.speed(0)

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        #create road
        class Road(turtle.Turtle):
            
            def __init__(self,x,y,risk_up):
                turtle.Turtle.__init__(self)
                if risk_up:
                    self.shape(image_road[0])
                else:
                    self.shape(image_road[1])
                self.penup()
                self.speed(0)
                self.goto(x, y)

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        #create sideroad
        class SideRoad(turtle.Turtle):
            
            def __init__(self,x,y):
                turtle.Turtle.__init__(self)
                self.shape(sideroad)
                self.penup()
                self.speed(0)
                self.goto(x, y)

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        #create crossroad
        class CrossRoad(turtle.Turtle):
            
            def __init__(self,x,y):
                turtle.Turtle.__init__(self)
                self.shape(crossroad)
                self.penup()
                self.speed(0)
                self.goto(x, y)

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        #create semaphore
        class Semaphore(turtle.Turtle):
            
            def __init__(self,x,y):
                turtle.Turtle.__init__(self)
                self.shape(image_semaphore[0])
                self.penup()
                self.speed(0)
                self.goto(x, y)
                self.image = 0
            
            def change(self):
                #red
                if self.image == 0:
                    self.shape(image_semaphore[1])
                    self.image = 1
                #green
                else:
                    self.shape(image_semaphore[0])
                    self.image = 0
                
                turtle.ontimer(self.change, 3500)

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        #create car
        class Car(turtle.Turtle):
            
            def __init__(self,x,y,i):
                turtle.Turtle.__init__(self)
                self.shape(image_cars[i])
                self.penup()
                self.speed(0)
                self.goto(x, y)
                if i < 2:
                    self.direction = "left"
                else:
                    self.direction = "right"
            
            def move_cars(self):
                if ((self.xcor(),self.ycor()) == (-480,0)):
                    self.goto(480, 0)
                if ((self.xcor(),self.ycor()) == (-480,-24)):
                    self.goto(480, -24)
                if ((self.xcor(),self.ycor()) == (-480,-48)):
                    self.goto(480, -48)
                if ((self.xcor(),self.ycor()) == (480,-72)):
                    self.goto(-480, -72)
                if ((self.xcor(),self.ycor()) == (480,-96)):
                    self.goto(-480, -96)
                if ((self.xcor(),self.ycor()) == (480,-120)):
                    self.goto(-480, -120)

                if self.direction == "left":
                    x = -24
                    y = 0
                elif self.direction == "right":
                    x = 24
                    y = 0
                move_to_x = self.xcor() + x
                move_to_y = self.ycor() + y
                
                #semaphore red
                if semaphores[0].image == 0:
                    self.goto(move_to_x, move_to_y)
                
                #semaphore green
                else:
                    if self.xcor()>=-48 and self.xcor()<=24 and self.direction == "left":
                        self.goto(24, self.ycor())
                    elif self.xcor()>=-72 and self.xcor()<=0 and self.direction == "right":
                        self.goto(-72, self.ycor())
                    else:
                        self.goto(move_to_x, move_to_y)

                turtle.ontimer(self.move_cars, t = random.randint(100, 500))

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        #create buttons
        class Button(turtle.Turtle):
            
            def __init__(self,x,y):
                turtle.Turtle.__init__(self)
                self.shape(image_buttons[0])
                self.penup()
                self.speed(0)
                self.goto(x, y)

            def change_button(self):
                self.shape(image_buttons[1])

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        #create buttons
        class Door(turtle.Turtle):
            
            def __init__(self,direction,x,y):
                turtle.Turtle.__init__(self)
                self.penup()
                self.speed(0)
                self.goto(x, y)
                self.x = x
                self.y = y
                self.is_closed = True
                self.direction = direction

                if(direction == "V"):  #vertical
                    self.shape(image_doors[0])
                else:                  #horizontal
                    self.shape(image_doors[2])

            def opens(self):
                self.is_closed = False
                if(self.direction == "V"):  #vertical
                    self.shape(image_doors[1])
                else:
                    self.shape(image_doors[0])

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        #class person
        class Person(turtle.Turtle):
            
            def __init__(self, x, y):
                turtle.Turtle.__init__(self)
                self.shape(image_people[0])
                self.hp = -200
                self.penup()
                self.speed(0)
                self.gold = -25
                self.goto(x, y)
                self.direction = random.choice(["up", "down", "left", "right"])

            def move(self):
                if self.direction == "up":
                    self.shape(image_people[3])
                    x = 0
                    y = 24
                elif self.direction == "down":
                    self.shape(image_people[0])
                    x = 0
                    y = -24
                elif self.direction == "left":
                    self.shape(image_people[2])
                    x = -24
                    y = 0
                elif self.direction == "right":
                    self.shape(image_people[1])
                    x = 24
                    y = 0
                move_to_x = self.xcor() + x
                move_to_y = self.ycor() + y

                if not can_move(move_to_x, move_to_y, self, True):
                    self.direction = random.choice(["up", "down", "left", "right"])
                turtle.ontimer(self.move, t = random.randint(100, 500))

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()
    
        #setup level
        def setup_maze(level):
            for y in range(len(level)):
                for x in range(len(level[y])):
                    character = level[y][x]
                    position_x = -456 + (x * 24)
                    position_y = 288 - (y * 24)
                    if character == "X":
                        pen.goto(position_x, position_y)
                        pen.stamp()
                        walls.append((position_x, position_y))
                    #elif character == "T":
                        #treasures.append(Treasure(position_x, position_y))
                    #elif character == "H":
                        #bones.goto(position_x, position_y)
                    elif character == "B":
                        buttons.append(Button(position_x, position_y))
                        buttons_pos.append((position_x, position_y))
                    elif character == "D":
                        doors.append(Door("V",position_x, position_y))
                        doors_pos.append((position_x, position_y))
                    elif character == "A":
                        doors.append(Door("H",position_x, position_y))
                        doors_pos.append((position_x, position_y))
                    elif character == "R":
                        roads.append(Road(position_x, position_y, True))
                    elif character == "K":
                        roads.append(Road(position_x, position_y, False))
                    elif character == "Z":
                        sideroads.append(SideRoad(position_x, position_y))
                        side_pos.append((position_x, position_y))
                    elif character == "Y":
                        crossroads.append(CrossRoad(position_x, position_y))
                    elif character == "S":
                        semaphores.append(Semaphore(position_x, position_y)) 
                    elif character == "U":
                        available_pos.append((position_x, position_y))

        def setup_people_and_cars(level):
            for y in range(len(level)):
                for x in range(len(level[y])):
                    character = level[y][x]
                    position_x = -456 + (x * 24)
                    position_y = 288 - (y * 24)
                    #player - dog
                    #if character == "P":
                        #player.goto(position_x, position_y)
                    #people
                    if character == "E":
                        persons.append(Person(position_x, position_y))
                    #cars
                    elif character == "C":
                        cars.append(Car(position_x, position_y, 0))
                    elif character == "V":
                        cars.append(Car(position_x, position_y, 1))
                    elif character == "O":
                        cars.append(Car(position_x, position_y, 2))
                    elif character == "G":
                        cars.append(Car(position_x, position_y, 3))

        def set_player_treasures_bones(name_level):
            pos_treasure = []
            pos_player = 0 
            pos_bones = 0
            nr = 0
            if(name_level == "easy"):
                nr = 5
            elif(name_level == "medium"):
                nr = 10
            elif(name_level == "hard"):
                nr = 15

            while True:
                if(name_level == "medium"):
                    #por o player sempre assim na porta
                    y_door_pos = doors_pos[0][1]
                    while True:
                        pos_player = random.choice(available_pos)
                        if pos_player[1] > y_door_pos:
                            break
                else:
                    pos_player = random.choice(available_pos)

                pos_bones = random.choice(available_pos)
                
                for j in range(nr):
                    pos_treasure.append(random.choice(available_pos)) 

                if(pos_player != pos_bones):
                    break
            
            player.goto(pos_player)
            bones.goto(pos_bones)
            for j in range(nr):
                aux = pos_treasure[j]
                treasures.append(Treasure(aux[0],aux[1]))

        
        #create instance
        pen = Pen()
        bones = Bones()
        logo = LogoBlindoff()
        
        #Agents
        # randomAgent = agents.RandomAgent()
        # greedyAgent = agents.GreedyAgent()
        # qLearningAgent = agents.QLearningAgent()

        # agent = qLearningAgent
        
        #set up level
        setup_maze(map_level)

        player = Player()
        #set up people and cars
        setup_people_and_cars(map_level)

        #set up player, treaudres and bone
        set_player_treasures_bones(name_level)

        #keyboard bindding
        #turtle.listen()
        #turtle.onkey(player.up, "Up")
        #turtle.onkey(player.down, "Down")
        #turtle.onkey(player.right, "Right")
        #turtle.onkey(player.left, "Left")

        #run person
        for person in persons:
            turtle.ontimer(person.move, 250)
        
        #run cars
        for car in cars:
            turtle.ontimer(car.move_cars, 250)
        
        #run semaphore
        for sem in semaphores:
            turtle.ontimer(sem.change, 550)

        def player_dead():
            turtle.clearscreen()
            turtle.color('red')
            turtle.penup()
            turtle.goto(0, -45)
            style = ('Courier', 24, 'italic')
            turtle.write('You died! Play again', font=style, align='center')
            turtle.hideturtle()
            time.sleep(4)
            turtle.clearscreen()
            main.main()
            turtle.done()
        
        def player_win():
            turtle.clearscreen()
            turtle.color('blue')
            turtle.penup()
            turtle.goto(0, -45)
            style = ('Courier', 24, 'italic')
            turtle.write('You are winner!', font=style, align='center')
            turtle.hideturtle()
            time.sleep(4)
            turtle.clearscreen()
            main.main()
            turtle.done()
        
        def hit_car():
            for car in cars:
                if player.is_collision(car):
                    #player_dead()
                    return True
            return False

        def press_button():
            for i in range(len(buttons)):
                c=0
                button = buttons[i]
                if player.is_collision(button):
                    c+=1
                    #print("estou em cima do button")
                    #print(c)
                    button.change_button()
                    doors[i].opens()
        
        def get_treasure():
            for treasure in treasures:
                if player.is_collision(treasure):
                    player.hp += 300
                    #show_score(timer, player.n_steps, player.hp)
                    treasure.destroy()
                    treasures.remove(treasure)
                    return True
            return False

        def hit_people():
            for person in persons:
                if player.is_collision(person):
                    player.hp -= 400
                    #show_score(timer, player.n_steps ,player.hp)
                    person.destroy()
                    persons.remove(person)
                    if player.hp <= 0:
                        #player_dead()
                        return 0
                    else:
                        return 1
            return 2

        def make_action(action):
                if(action == 0):
                    player.down()
                if(action == 1):
                    player.left()
                if(action == 2):
                    player.up()
                if(action == 3):
                    player.right()
                if(action == 4):
                    pass
        
        def treasures_to_positions():
            pos_treasure = []
            for treasure in treasures:
                pos_treasure.append([treasure.xcor(),treasure.ycor()])
            if(map_level == "medium"):
                for button_pos in buttons_pos:
                    pos_treasure.append(button_pos)
            return pos_treasure

        def step(action):
            next_obs = []
            terminal = False
            reward = 0

            make_action(action)
            timer = int(time.time()) - int(start)
            show_score(timer, player.n_steps, player.hp)

            if press_button():
                reward = 1
            
            if hit_car():
                reward = -1
                terminal = True
            
            if get_treasure():
                reward = 1

            if hit_people() == 0:
                reward = -1
                terminal = True
            elif hit_people() == 1:
                reward = -1

            if player.is_collision(bones) and len(treasures) == 0:
                #player_win()
                reward = 2
                terminal = True

            next_obs = treasures_to_positions()

            if next_obs == [] and player.xcor() != bones.xcor() and player.ycor() != bones.ycor():
                next_obs.append([bones.xcor(),bones.ycor()])

            return next_obs,reward,terminal   
        
        terminal = False
        observation = treasures_to_positions()
        if (agent.name == "Q-Learning"):
                if(agent._exploration_rate <= 0.01):
                    agent.eval()
                    agent._exploration_rate = 0.01
                else:
                    agent.train()
                    agent._exploration_rate = agent._exploration_rate - 0.30
        
        while not terminal:
            agent.see(observation)
            action = agent.action(player.xcor(),player.ycor(),walls)
            next_obs, reward, terminal = step(action)
            if agent.train():
                agent.next(observation, action, next_obs, reward, terminal)               
            observation = next_obs
            screen.update()

        return player.n_steps
    #except:
        #to avoid the erro from trying to update a screen that has already been destroyed
        #print("The screen is dead.")
              

  
