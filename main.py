import time
import random
import turtle

window = turtle.Screen()
window.bgcolor("light blue")
window.title("Catch the Turtle")

#create turtle
turtle_shape = turtle.Turtle()
turtle_shape.shape("turtle")

#score text
score = 0
score_text = turtle.Turtle()
score_text.penup()
score_text.goto(0,window.window_height() // 2 - 50)
score_text.color("blue")
score_text.write(f"Score: {score}", align="center", font=("Arial",16,"bold"))
#skoru arttırma
def increase_score(x,y):
    global score
    score+=1
    score_text.clear()
    score_text.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

#zamanlayıcı oluşturma
counter = 15
#time text
counter_text = turtle.Turtle()
counter_text.color("red")
counter_text.penup()
counter_text.goto(0, window.window_height() // 2 - 80 )
#counter update func.
def update_counter():
    global counter
    counter_text.clear()
    counter_text.write(f"Time: {str(counter)}", align="center", font=("Arial", 16, "bold"))
    counter -= 1
    if counter >= 0:
        #rastgele konum belirleme
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        turtle_shape.penup()
        turtle_shape.goto(x,y)
        window.ontimer(update_counter,1000)

#show first counter value
update_counter()

window.delay(10)

#turtle'a tıklandığında score'u arttırır
turtle_shape.onclick(increase_score)

window.mainloop()
