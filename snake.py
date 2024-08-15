from turtle import Turtle

# CONSTANT VALUE
# creating constant value makes easier to change the starting pos, move distance without affecting the body of the code.
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment_list = []
        self.create_snake()    # can run even the create_snake method is created below the __init__.
        self.head = self.segment_list[0]
        # once class snake is initialized. create snake method will be executed.

    def create_snake(self):
        """create 3 object lined up horizontally on starting position."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """add a segment to a given position."""
        new_segment = Turtle("square")  # create multiple object.
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment_list.append(new_segment)

    def extend(self):
        """add a segment to the last position of segments list."""
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        """move the object forward continuously, following the first segment."""
        for seg_num in range(len(self.segment_list) - 1, 0, -1):  # start, stop(excluded), step.
            new_x = self.segment_list[seg_num - 1].xcor()
            new_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(x=new_x, y=new_y)  # from last segment to before first, will follow
            # the position of their front.

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:    # prevent snake to go in opposite direction.
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
