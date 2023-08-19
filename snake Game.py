import turtle
import random
import time

# 1.setting up the game screen

screen = turtle.Screen()
screen.title("Snake game project")
screen.setup(width = 700, height = 700)
screen.tracer(0)
screen.bgcolor("#7393B3")

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-350, 357)
turtle.pendown()
turtle.forward(700)
turtle.right(90)
turtle.forward(700)
turtle.right(90)
turtle.forward(700)
turtle.right(90)
turtle.forward(700)
turtle.penup()
turtle.hideturtle()

# 2.Initializing the game
# score
score = 0;
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Red")
food.penup()
food.goto(30, 30)

# collection
food_collection = []

# points
points = turtle.Turtle()
points.speed(0)
points.color("white")
points.penup()
points.hideturtle()
points.goto(-240, 290)
points.write("Score: ",align = "center", font = ("calibri", 25, "bold"))

# movements
def move_up():
    if snake.direction!= "down":
        snake.direction = "up"

def move_down():
    if snake.direction!= "up":
        snake.direction = "down"

def move_left():
    if snake.direction!= "right":
        snake.direction = "left"

def move_right():
    if snake.direction!= "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# user input

screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# 3.GAME LOOP

while True:
    screen.update()
    
    
    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.goto(x, y)
        points.clear()
        score += 1
        points.write("Score : {}".format(score), align = "center", font = ("calibri", 25, "bold"))
        delay -= 0.001


    # new food generation
        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape("square")
        new_food.color("white")
        new_food.penup()
        food_collection.append(new_food)

    #snake new body

    for index in range(len(food_collection) -1, 0, -1):
        a = food_collection[index -1].xcor()
        b = food_collection[index -1].ycor()

        food_collection[index].goto(a, b)

    if len(food_collection) > 0:
        a = snake.xcor()
        b = snake.ycor()
        food_collection[0].goto(a, b)
    snake_move()
    
    # 4.COLLISON DETECTION

        # 5.GAME OVER CONDITION
    if snake.xcor() > 340 or snake.xcor() < -340 or snake.ycor() > 340 or snake.ycor() < -340:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("black")
        points.goto(0, 0)
        points.write("Game Over \n Your Score {}".format(score), align = "center", font = ("calibri", 30, "bold"))

    
    for foods in food_collection:
        if foods.distance(snake)<20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("magenta")
            points.goto(0, 0)
            points.write("Game Over \n Your Score {}".format(score), align = "center", font = ("calibri", 30, "bold"))

    time.sleep(delay)

turtle.Terminator()