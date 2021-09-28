
import turtle
import random
import time
points = 0
delay = 0.1 #delay for the execution of code
old_food = []

# creating a screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.tracer(0)
screen.setup (width = 400, height = 360)
screen.bgcolor("green")

# creating border
turtle.speed(4)
turtle.pensize(3)
turtle.penup()
turtle.goto(-150,150)
turtle.pendown()
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.penup()
turtle.hideturtle()

# creating snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('triangle')
snake.color('blue')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop' # to stop moving after coming to 0,0

# creating food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('orange')
food.penup()
food.goto(30,30)

# creating score text
score = turtle.Turtle()
score.speed(0)
score.color('black')
score.penup()
score.goto(0,300)
score.write('SCORE : ', align = 'center', font = ('calibri', 16, 'bold'))

# defining snake movement
def snake_go_up():
    if snake.direction != 'down':
        snake.direction = 'up'
def snake_go_right():
    if snake.direction != 'left' : 
        snake.direction = 'right'
def snake_go_down():
    if snake.direction != 'up' : 
        snake.direction = 'down'
def snake_go_left():
    if snake.direction != 'right' : 
        snake.direction = 'left'
def snake_move():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x+20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x-20)

screen.listen() # listen = listens to our key presses
screen.onkeypress(snake_go_up, 'Up')
screen.onkeypress(snake_go_down, 'Down')
screen.onkeypress(snake_go_left, 'Left')
screen.onkeypress(snake_go_right, 'Right')

# main loop
while True:
    screen.update()
    # snake and fruit collision
    if snake.distance(food) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        food.goto(x,y)
        score.clear() 
        points +=1 # to increase score by 1
        score.write('SCORE : {}'.format(points), align = 'center', font = ('calibri', 16, 'bold'))
        delay -= 0.001 # to make the game faster
        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape('circle')
        new_food.color('orange')
        new_food.penup()
        old_food.append(new_food)  # append = add
    for f in range(len(old_food)- 1, 0, -1):
        a = old_food[f-1].xcor() 
        b = old_food[f-1].ycor() 
        old_food[f].goto(a,b)
    if len(old_food) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_food[0].goto(a,b)
    snake_move() # calling of function
    # snake and border collision
    if snake.xcor() > 150 or snake.xcor() < -150 or snake.ycor() > 150 or snake.ycor() < -150:
        time.sleep(1) 
        screen.clear()
        screen.bgcolor('green')
        score.goto(0,0)
        score.write('GAME OVER\n YOUR SCORE IS : {}'.format(points), align = 'center', font = ('calibri', 16, 'bold'))
    for f in old_food:
        if f.distance(snake) < 20:
            time.sleep(1) 
            screen.clear()
            screen.bgcolor('green')
            score.goto(0,0)
            score.write('GAME OVER\n YOUR SCORE IS : {}'.format(points), align = 'center', font = ('calibri', 16, 'bold'))
    time.sleep(delay)
turtle.Terminator() # terminating the program