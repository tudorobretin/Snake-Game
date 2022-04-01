from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.squares_list = []
        self.posx = 0
        self.move_or_not = 0
        self.snake_speed = 10
        self.create_snake()
        self.head = self.squares_list[0]

    def reset(self):
        for segment in self.squares_list:
            segment.goto(1000, 1000)
        self.squares_list.clear()
        self.create_snake()
        self.head = self.squares_list[0]
        self.snake_speed = 10

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares_list.append(new_square)

    def extend(self):
        self.add_segment(self.squares_list[-1].position())

    def up(self, screen):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def speed_increase(self):
        if self.snake_speed>1:
            self.snake_speed -= 0.5

    def move(self):
        self.move_or_not += 0.5
        if self.move_or_not == self.snake_speed:
            self.move_or_not = 0
            for i in range(len(self.squares_list) - 1, 0, -1):
                second_pos = self.squares_list[i - 1].pos()
                self.squares_list[i].setposition(second_pos)
            self.head.forward(20)