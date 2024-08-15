from turtle import Screen
import scoreboard
import food
import snake
import time


screen = Screen()
screen_x = 600
screen_y = 600
screen.setup(screen_x, screen_y)
screen.bgcolor("black")
screen.title("CARL SNAKE GAME PROJECT")
screen.tracer(0)  # show/hide the turtle object at start. 0=hide, 1=show
screen.listen()

# TODO create snake (3 object).
snake = snake.Snake()

# TODO create a score board.
score = scoreboard.Scoreboard()

# TODO : create food.
food = food.Food()

# TODO control the snake.
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


# TODO move the snake.
is_game_on = True
while is_game_on:
    screen.update()  # refresh the screen
    time.sleep(0.1)  # set screen animation delay. refresh every 0.1sec.
    snake.move()    # move forward continuously.

    # TODO detect collision with food.
    if snake.head.distance(food) < 16:  # distance method. return the gap distance between head and food.
        food.refresh()
        snake.extend()
        score.increase_score()    # clear score, add one then show updated score value.

    # TODO detect collision with wall. (GAME OVER).
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # TODO detect collision with tail. (GAME OVER).
    for segment in snake.segment_list[1:]:  # loop excluding the first segment.
        if snake.head.distance(segment) < 10:   # distance between head and segments.
            is_game_on = False
            score.game_over()


screen.exitonclick()
