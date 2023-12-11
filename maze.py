import turtle  # import turtle library
import time

wn = turtle.Screen()  # define the turtle screen
wn.bgcolor("gray")  
wn.title("Maze")
wn.setup(1300, 700)  

# declare system variables

startPossition = [];

start_x = 0
start_y = 0
end_x = 0
end_y = 0

grid1 = [
    "++++++++++++++++++++++++++++++++++",
    "+      +++           ++++++++B   +",
    "+++++++++++++++ +++++++++++++ ++ +",
    "++A          ++                + +",
    "++ +++ ++ ++++++++++++++++++ + + +",
    "++ +++ ++ +++++              + + +",
    "++ +++ ++ +++++ ++++++++++++ + +++",
    "++ +++ ++ +   +            + + +++",
    "++ +++ ++ + + ++++++++++++ +    ++",
    "++ +++ ++ + + +            +++++++",
    "++ +++ ++ + + + +++++++++++++    +",
    "++ +++ ++   + +         ++ ++ ++ +",
    "++ +++ +++++++++++++++++++ ++ ++ +",
    "++ +++     +     +            ++ +",
    "++++++++++++ +++ + +++++++ ++ ++ +",
    "++           +  U  +       +++++ +",
    "++ +++++++++++++++++++++++++     +",
    "++                     ++    +++++",
    "++++++++++++++++++++++ ++ ++++++++",
    "++                     ++    +   +",
    "++ +++++++++++++++++++++++++ + + +",
    "++          ++++   +++         + +",
    "+++++++++++ +++++ ++++++++++++++ +",
    "++          +++++   ++      Z    +",
    "+++++++Y++++++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++++++",
]


class Maze(turtle.Turtle):  # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.ht()
        self.shape("square")  
        self.color("black")  
        self.penup()  # lift up the pen so it do not leave a trail
        self.speed(0)  # define the animation speed



# use green turtles to show the visited cells
class Green(turtle.Turtle):  # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.ht()
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


# use blue turtle to show the frontier cells and to draw shortest path
class Blue(turtle.Turtle):  # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.ht()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# use the red turtle to represent the start position
class Red(turtle.Turtle):  # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.ht()
        self.shape("square")
        self.color("red")
        self.setheading(270)  # point turtle to point down
        self.penup()
        self.speed(0)


# use the yellow turtle to represent the end position
class Yellow(turtle.Turtle):  # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.ht()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


class Button(turtle.Turtle):
    def __init__(self, num, color):
        super().__init__(shape='square', visible=False)
        self.num = num
        self.color(color)
        self.penup()

    def click(self, x, y):
        global visited, found
        dfs(startPossition[self.num - 1][0], startPossition[self.num - 1][1])
        self.clear()
        if found == 0:
            turtle.ht()
            turtle.penup()
            turtle.color("red")
            turtle.goto(240, 20)
            turtle.write("Malheuresement, vous n'avez \n pas trouvé le trésor !", font=("Arial", 16, "normal"))
            time.sleep(3)
            turtle.undo()
            turtle.ht()
            green.clear()
            blue.clear()
        visited.clear()
        found = 0


def setup_maze(grid):
    global end_x, end_y  # set up global variables for start and end locations
    for y in range(len(grid)):  # iterate through each line in the grid
        for x in range(len(grid[y])):  # iterate through each character in the line
            time.sleep(0)
            character = grid[y][x]  # assign the variable character to the y and x positions of the grid
            screen_x = -600 + (x * 24)  # move to the x location on the screen staring at -600
            screen_y = 288 - (y * 24)  # move to the y location of the screen starting at 288

            if character == "+":  # if character contains a '+'
                maze.goto(screen_x, screen_y)  # move pen to the x and y location
                maze.stamp()  # stamp a copy of the white turtle on the screen
                walls.append((screen_x, screen_y))  # add cell to the walls list

            if character == " ":  # if no character found
                path.append((screen_x, screen_y))  # add to path list

            if character == "U":  # if cell contains an 'U'
                yellow.goto(screen_x, screen_y)  # move pen to the x and y location
                yellow.stamp()  # stamp a copy of the yellow turtle on the screen
                end_x, end_y = screen_x, screen_y  # assign end locations variables to end_x and end_y
                path.append((screen_x, screen_y))  # add cell to the path list

            if character == "A" or character == "B" or character == "Y" or character == "Z":  # if cell contains a "i"
                startPossition.append((screen_x, screen_y))  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)  # send red turtle to start position
                red.stamp()

            # Depth-first search


def dfs(x, y):
    global found  # found is used to indicate if we reach the end cell or not
    if found == 1:
        return
    visited.add((x, y))  # add current cell to visited list
    green.goto(x, y)  # green turtle goto x and y position
    green.stamp()  # stamp a copy of the green turtle on the maze
    if x == end_x and y == end_y:
        found = 1  # end cell found
        turtle.penup()
        turtle.color("red")
        turtle.goto(240, 20)
        turtle.write("Bravo, vous avez trouvé le trésor !", font=("Arial", 16, "normal"))
        time.sleep(3)
        turtle.undo()
        turtle.ht()
        green.clear()
        blue.clear()
        return
    for i in range(4):  # check UP/DOWN/LEFT/RIGHT
        child = (x + dx[i], y + dy[i])
        if child in path and child not in visited and not found:  # check child
            blue.goto(child)  # blue turtle goto child
            blue.stamp()
            dfs(x + dx[i], y + dy[i])


turtle.ht()
turtle.speed(0)
turtle.penup()
turtle.goto(380, 300)
turtle.color("black")
turtle.write("Choisir une entrée:", font=("Arial", 12, "normal"))

# Create the buttons
button1 = Button(1, 'red')
button2 = Button(2, 'red')
button3 = Button(3, 'red')
button4 = Button(4, 'red')


# Position the buttons on the screen
button1.goto(400, 250)

button2.goto(400, 210)

button3.goto(500, 250)

button4.goto(500, 210)





# Show the buttons +labels
turtle.ht()
turtle.goto(370, 230)
turtle.write("A", font=("Arial", 8, "normal"))
button1.showturtle()
turtle.goto(370, 200)
turtle.write("B", font=("Arial", 8, "normal"))
button2.showturtle()
turtle.goto(470, 230)
turtle.write("Y", font=("Arial", 8, "normal"))
button3.showturtle()
turtle.goto(470, 200)
turtle.write("Z", font=("Arial", 8, "normal"))
button4.showturtle()
turtle.penup()
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
walls = []
path = []
visited = set()  # A hash table for search and insert cell in O(1) complexity
dy = [24, 0, -24, 0]  # navigate between child of cell
dx = [0, 24, 0, -24]
found = 0
setup_maze(grid1)  # call setup maze function

# Set the button click functions
button1.onclick(button2.click)
button2.onclick(button1.click)
button3.onclick(button4.click)
button4.onclick(button3.click)


turtle.mainloop()  # waits for the input from user



