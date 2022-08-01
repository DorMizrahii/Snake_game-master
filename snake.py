import turtle as t

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {"Up": 90, "Down": 270, "Left": 180, "Right": 0}
OFFSET = 12


class Snake:
    my_snakes = []

    def __init__(self):
        for coordinate in STARTING_POSITION:
            new_snake = t.Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(coordinate)
            self.my_snakes.append(new_snake)
        self.head = self.my_snakes[0]

    def move(self):
        my_snakes_length = len(self.my_snakes) - 1
        for i in range(my_snakes_length, 0, - 1):
            new_x = self.my_snakes[i - 1].xcor()
            new_y = self.my_snakes[i - 1].ycor()
            self.my_snakes[i].goto(new_x, new_y)
        self.my_snakes[0].forward(MOVE_DISTANCE)
        self.my_snakes[0].color("red")
        self.my_snakes[0].shape("triangle")


    def extend(self):
        new_snake = t.Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(self.head.xcor(), self.head.ycor())
        self.my_snakes.append(new_snake)

    def up(self):
        if self.head.heading() != DIRECTIONS["Down"]:
            self.head.setheading(DIRECTIONS["Up"])

    def down(self):
        if self.head.heading() != DIRECTIONS["Up"]:
            self.head.setheading(DIRECTIONS["Down"])

    def right(self):
        if self.head.heading() != DIRECTIONS["Left"]:
            self.head.setheading(DIRECTIONS["Right"])

    def left(self):
        if self.head.heading() != DIRECTIONS["Right"]:
            self.head.setheading(DIRECTIONS["Left"])

    def out_of_bound(self):
        return (-280 <= self.head.xcor() <= 280) and (-280 <= self.head.ycor() <= 280)

    def mistake_coordinates(self):
        if self.head.xcor() >= 0 and self.head.ycor() >= 0:
            return self.head.xcor() - OFFSET, self.head.ycor() - OFFSET
        elif self.head.xcor() >= 0 and self.head.ycor() <= 0:
            return self.head.xcor() - OFFSET, self.head.ycor() + OFFSET
        elif self.head.xcor() <= 0 and self.head.ycor() >= 0:
            return self.head.xcor() + OFFSET, self.head.ycor() - OFFSET
        else:
            return self.head.xcor() + OFFSET, self.head.ycor() + OFFSET

    def is_touching(self):

        for snake in self.my_snakes[1:]:
            if self.head.distance(snake) < 15:
                return True
        return False
