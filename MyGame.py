import time
import turtle
from random import randint, choice


class Game:
    def __init__(self):  # позицията
        self.points_b = 0
        self.points_a = 0
        self.width = 1100
        self.height = 600
        self.__ball_pos = (randint(-300, 300), randint(-300, 300))
        self.ball_delta_x = 1
        self.ball_delta_y = 1

        self.paddle_a_pos = (-self.width / 2 + 10, 0)
        self.paddle_b_pos = (self.width / 2 - 20, 0)
        self.paddle_height = self.height * 0.20
        self.paddle_width = 20

    def tick(self):  # цъкането
        self.board_check()
        self.preform_paddle_hit()
        x, y = self.__ball_pos
        self.__ball_pos = (x + self.ball_delta_x, y + self.ball_delta_y)

    def ball_pos(self):  # връща позицията
        return self.__ball_pos

    def preform_paddle_hit(self):
        x, y = self.__ball_pos
        a_x, a_y = self.paddle_a_pos
        hit_a = (a_x + self.paddle_width) == x and (a_y - self.paddle_height / 2 <= y <= (a_y + self.paddle_height / 2))
        if hit_a:
            self.ball_delta_x *= -1

        b_x, b_y = self.paddle_b_pos
        hit_b = (b_x - self.paddle_width) == x and (b_y - self.paddle_height / 2 <= y <= (b_y + self.paddle_height / 2))
        if hit_b:
            self.ball_delta_x *= -1

    def board_check(self):  # рикушет на топчето
        x, y = self.__ball_pos
        if abs(y) >= self.height / 2:
            self.ball_delta_y *= -1
        if x <= (-self.width / 2):
            self.points_b += 1
            self.ball_delta_x *= choice([-1, 1])
            self.__ball_pos = ((randint(-300, 300)* self.ball_delta_x), randint(-300, 300))
            self.ball_delta_x *= choice([-1, 1])
        elif x >= (self.width / 2):
            self.points_a += 1
            self.ball_delta_x *= choice([-1, 1])
            self.__ball_pos = ((randint(-300, 300)*self.ball_delta_x), randint(-300, 300))


    def paddle_a_up(self):
        x, y = self.paddle_a_pos
        self.paddle_a_pos = (x, y+50)

    def paddle_a_down(self):
        x, y = self.paddle_a_pos
        self.paddle_a_pos = (x, y-50)

    def paddle_b_up(self):
        x, y = self.paddle_b_pos
        self.paddle_b_pos = (x, y+50)

    def paddle_b_down(self):
        x, y = self.paddle_b_pos
        self.paddle_b_pos = (x, y-50)

prev_a = None
prev_b = None

game = Game()

screen = turtle.Screen()
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)
screen.setup(game.width, game.height)
screen.bgcolor("Black")
screen.title("Pong Game by Alex Draganov")
player_a = screen.textinput("Name A", "Your Name, player A")
player_b = screen.textinput("Name B", "Your Name, player B")
title = turtle.TurtleScreen

pen = turtle.Turtle()  # точките
pen.color("Yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score {player_a}: {game.points_a} <<:|:>>  Score {player_b}: {game.points_b}", align="center", font=("Courier", 24, "normal"))

ball = turtle.Turtle()
ball.color("Red")
ball.shape("circle")
ball.penup()

paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("Green")
paddle_a.penup()
paddle_a.goto(game.paddle_a_pos)
paddle_a.shapesize(game.paddle_height / 20, game.paddle_width / 20)

paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("Blue")
paddle_b.penup()
paddle_b.goto(game.paddle_b_pos)
paddle_b.shapesize(game.paddle_height / 20, game.paddle_width / 20)


def player_a_up():
    game.paddle_a_up()


def player_a_down():
    game.paddle_a_down()


def player_b_up():
    game.paddle_b_up()


def player_b_down():
    game.paddle_b_down()


screen.listen()
screen.onkeypress(player_a_up, "w")
screen.onkeypress(player_a_down, "s")
screen.onkeypress(player_b_up, "Up")
screen.onkeypress(player_b_down, "Down")

while True:
    game.tick()
    ball.goto(game.ball_pos())
    paddle_a.goto(game.paddle_a_pos)
    paddle_b.goto(game.paddle_b_pos)
    if prev_a != game.points_a or prev_b != game.points_b:
        pen.clear()
        pen.write(f"Score {player_a}: {game.points_a} <<:|:>>  Score {player_b}: {game.points_b}", align="center", font=("Courier", 24, "normal"))

    screen.update()
    time.sleep(0.001)
