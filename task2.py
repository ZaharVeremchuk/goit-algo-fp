import turtle

def draw_pifagor_tree(len, level):
    if level == 0:
        return
    turtle.forward(len)
    turtle.right(45)
    draw_pifagor_tree(0.8 * len, level - 1)
    turtle.left(90)
    draw_pifagor_tree(0.8 * len, level - 1)
    turtle.right(45)
    turtle.backward(len)


def display(level):
    turtle.bgcolor("red")
    turtle.left(90)
    turtle.speed(0)
    turtle.color("green")
    draw_pifagor_tree(len=80, level=level) 
    turtle.hideturtle()
    turtle.done()


# Налаштування вікна та черепашки
screen = turtle.Screen()
screen.setup(800, 600)
turtle.speed(0)
turtle.penup()
turtle.goto(-100, -200)
turtle.pendown()

# Запитуємо рівень рекурсії у користувача
level = int(input("Введіть рівень рекурсії: "))

# Малюємо дерево Піфагора
display(level)

turtle.done()