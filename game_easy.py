#thaycacac
import turtle
import math
import random
import main

def init_game(name_level, map_level):
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("A Maze Game")
    screen.setup(1000, 750)
    screen.tracer(0)

    #register shape
    wall_easy = "wall_easy.gif"
    screen.addshape(wall_easy)
    wall_medium = "wall_medium.gif"
    screen.addshape(wall_medium)
    wall_hard = "wall_hard.gif"
    screen.addshape(wall_hard)
    image_princess = "princess.gif"
    screen.addshape(image_princess)
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
    image_monsters = ["monster_0.gif", "monster_1.gif", "monster_2.gif", "monster_3.gif", "monster_4.gif"]
    for i in range(5):
        screen.addshape(image_monsters[i])
    image_treasures = ["treasure_0.gif", "treasure_1.gif", "treasure_2.gif", "treasure_3.gif", "treasure_4.gif"]
    for i in range(5):
        screen.addshape(image_treasures[i])
    
    # create list
    walls = []
    treasures = []
    monsters = []

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
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def down(self):
            self.shape(bottom)
            move_to_x = self.xcor()
            move_to_y = self.ycor() - 24
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def left(self):
            self.shape(left)
            move_to_x = self.xcor() - 24
            move_to_y = self.ycor()
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def right(self):
            self.shape(right)
            move_to_x = self.xcor() + 24
            move_to_y = self.ycor()
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

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

    #create princess
    class Princess(turtle.Turtle):
        
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape(image_princess)
            self.penup()
            self.speed(0)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    #class monster
    class Monster(turtle.Turtle):
        
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            if name_level == "easy":
                self.number_random = random.randint(0, 1)
            elif name_level == "medium":
                self.number_random = random.randint(0, 2)
            else:
                self.number_random = random.randint(3, 4)
            self.shape(image_monsters[self.number_random])
            self.hp = -(self.number_random + 1) * 100
            self.penup()
            self.speed(0)
            self.gold = -25
            self.goto(x, y)
            self.direction = random.choice(["up", "down", "left", "right"])

        def move(self):
            if self.direction == "up":
                x = 0
                y = 24
            elif self.direction == "down":
                x = 0
                y = -24
            elif self.direction == "left":
                x = -24
                y = 0
            elif self.direction == "right":
                x = 24
                y = 0
            move_to_x = self.xcor() + x
            move_to_y = self.ycor() + y

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            else:
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
                    monsters.append(Monster(position_x, position_y))
                elif character == "H":
                    princess.goto(position_x, position_y)
                    princess.stamp()

    #create instance
    pen = Pen()
    player = Player()
    princess = Princess()
    logo = LogoBlindoff()
    randomAgent = RandomAgent()

    #keyboard bindding
    #turtle.listen()
    #turtle.onkey(player.up, "Up")
    #turtle.onkey(player.down, "Down")
    #turtle.onkey(player.right, "Right")
    #turtle.onkey(player.left, "Left")

    #set up level
    setup_maze(map_level)

    #run monster
    for monster in monsters:
        turtle.ontimer(monster.move, 250)

    while True:
        randomAgent.make_action(player)
        for treasure in treasures:
            if player.is_collision(treasure):
                player.hp += treasure.hp
                show_hp(player.hp)
                treasure.destroy()
                treasures.remove(treasure)
        for monster in monsters:
            if player.is_collision(monster):
                player.hp += monster.hp
                show_hp(player.hp)
                monster.destroy()
                monsters.remove(monster)
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
        if player.is_collision(princess) and len(treasures) == 0:
            turtle.clearscreen()
            turtle.color('blue')
            turtle.penup()
            turtle.goto(0, -45)
            style = ('Courier', 24, 'italic')
            turtle.write('You are winner!', font=style, align='center')
            turtle.hideturtle()
            main.main()
            turtle.done()
            break
        screen.update()
