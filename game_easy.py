#thaycacac
import turtle
import math
import random
import main
import time

def init_game(name_level, map_level):
    #try:
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("Blindoff")
        screen.setup(1000, 750)
        screen.tracer(0)

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
        
        # create list
        walls = []
        treasures = []
        persons = []
        buttons = []
        doors = []
        buttons_pos = []
        doors_pos = []

        #show hp
        def show_hp(hp):
            turtle.clear()
            turtle.color('white')
            turtle.penup()
            turtle.goto(380, 305)
            style = ('Courier', 20, 'bold')
            turtle.write("HP: {0}".format(hp), font=style, align='center')
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

        def can_move(move_to_x, move_to_y, player):
            if (move_to_x, move_to_y) not in walls and (move_to_x, move_to_y) not in doors_pos:
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
                show_hp(self.hp)

            def up(self):
                self.shape(top)
                move_to_x = self.xcor()
                move_to_y = self.ycor() + 24
                can_move(move_to_x, move_to_y, self)

            def down(self):
                self.shape(bottom)
                move_to_x = self.xcor()
                move_to_y = self.ycor() - 24
                can_move(move_to_x, move_to_y, self)

            def left(self):
                self.shape(left)
                move_to_x = self.xcor() - 24
                move_to_y = self.ycor()
                can_move(move_to_x, move_to_y, self)

            def right(self):
                self.shape(right)
                move_to_x = self.xcor() + 24
                move_to_y = self.ycor()
                can_move(move_to_x, move_to_y, self)

            def is_collision(self, other):
                a = self.xcor() - other.xcor()
                b = self.ycor() - other.ycor()
                distance = math.sqrt((a ** 2) + (b ** 2))
                if distance < 5:
                    return True
                else:
                    return False

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

                if not can_move(move_to_x, move_to_y, self):
                    self.direction = random.choice(["up", "down", "left", "right"])
                turtle.ontimer(self.move, t = random.randint(100, 300))

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
                    elif character == "P":
                        player.goto(position_x, position_y)
                    elif character == "T":
                        treasures.append(Treasure(position_x, position_y))
                    elif character == "E":
                        persons.append(Person(position_x, position_y))
                    elif character == "H":
                        bones.goto(position_x, position_y)
                        bones.stamp()
                    elif character == "B":
                        buttons.append(Button(position_x, position_y))
                        buttons_pos.append((position_x, position_y))
                    elif character == "D":
                        doors.append(Door("V",position_x, position_y))
                        doors_pos.append((position_x, position_y))
                    elif character == "A":
                        doors.append(Door("H",position_x, position_y))
                        doors_pos.append((position_x, position_y))

        #create instance
        pen = Pen()
        player = Player()
        bones = Bones()
        logo = LogoBlindoff()
        randomAgent = RandomAgent()

        #keyboard bindding
        turtle.listen()
        turtle.onkey(player.up, "Up")
        turtle.onkey(player.down, "Down")
        turtle.onkey(player.right, "Right")
        turtle.onkey(player.left, "Left")

        #set up level
        setup_maze(map_level)

        #run person
        for person in persons:
            turtle.ontimer(person.move, 250)

        while True:
            #randomAgent.make_action(player)

            for i in range(len(buttons)):
                c=0
                button = buttons[i]
                if player.is_collision(button):
                    c+=1
                    print("estou em cima do button")
                    print(c)
                    button.change_button()
                    doors[i].opens()

            for treasure in treasures:
                if player.is_collision(treasure):
                    player.hp += treasure.hp
                    show_hp(player.hp)
                    treasure.destroy()
                    treasures.remove(treasure)
            for person in persons:
                if player.is_collision(person):
                    player.hp += person.hp
                    show_hp(player.hp)
                    person.destroy()
                    persons.remove(person)
                    if player.hp <= 0:
                        turtle.clearscreen()
                        turtle.color('red')
                        turtle.penup()
                        turtle.goto(0, -45)
                        style = ('Courier', 24, 'italic')
                        turtle.write('You died! Play again', font=style, align='center')
                        turtle.hideturtle()
                        main.main()
                        turtle.done()
                        break
            if player.is_collision(bones) and len(treasures) == 0:
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
                break
            screen.update()
    #except:
        #to avoid the erro from trying to update a screen that has already been destroyed
        #print("The screen is dead.")
              

  
