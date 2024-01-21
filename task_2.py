import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def draw_full_snowflake(t, order, size):
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

def main():
    recursion_level = int(input("Enter the recursion level for the Koch snowflake: "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Koch Snowflake")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)
    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()
    snowflake_turtle.left(60)

    screen.tracer(0)

    draw_full_snowflake(snowflake_turtle, recursion_level, 300)

    screen.update()

    screen.exitonclick()

if __name__ == "__main__":
    main()
