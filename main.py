import time
import random
import turtle

window = turtle.Screen()
window.bgcolor("light blue")
window.title("Catch the Turtle")

#create turtle
turtle_shape = turtle.Turtle()
turtle_shape.shape("turtle")
score_text = turtle.Turtle()
counter_text = turtle.Turtle()

score=0
FONT = ('Arial', 16, 'normal')

def create_score_text():
    global score_text
    score_text.hideturtle()
    score = 0
    score_text.penup()

    #score_text.goto(0,window.window_height() // 2 - 50)
    top_height = window.window_height() / 2  # positive height/2 is the top of the screen
    y = top_height * 0.8  # decreasing a bit so text will be visible

    score_text.setpos(0, y)
    score_text.color("blue")
    score_text.write(f"Score: {score}", align="center", font=FONT)

def increase_score(x,y):
    global score, score_text
    score+=1
    score_text.clear()
    score_text.write(f"Score: {score}", align="center", font=FONT)

def create_count_down_text():

    top_height = window.window_height() / 2
    y_position = top_height - top_height / 10

    counter_text.hideturtle()
    counter_text.color("red")
    counter_text.penup()
    counter_text.setposition(0, y_position)
    counter_text.clear()

def hide_real_turtles():
    turtle_shape.hideturtle()

def show_turtles_randomly():
    # rastgele konum belirleme
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle_shape.penup()
    turtle_shape.goto(x, y)
    window.ontimer(show_turtles_randomly, 500)

#counter update func.
counter = 15
def update_counter():
    global counter

    create_count_down_text()

    counter_text.write(f"Time: {str(counter)}", align="center", font=FONT)
    counter -= 1

    if counter >= 0:
        window.ontimer(update_counter,1000)
    else:
        counter_text.clear()
        #hide turtles
        hide_real_turtles()
        counter_text.write(arg="Game over!", align="center", font=FONT)

def start_game_up():
    turtle.tracer(0)
    create_score_text()
    show_turtles_randomly()
    update_counter()#show first counter value
    window.delay(10)
    turtle_shape.onclick(increase_score)
    turtle.tracer(1)

start_game_up()

window.mainloop()
