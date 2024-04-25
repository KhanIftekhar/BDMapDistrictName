import turtle
import pandas as pd

FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.setup(width=700, height=800)
screen.title("Bangladesh District Name Game")
image = "BDMAPZ.gif"
turtle.addshape(image)
turtle.shape(image)

correct_answer = 0

df = pd.read_csv("Corr1.csv")

districts_name = df["District"].to_list()

x_cor = df["x"].to_list()
y_cor = df["y"].to_list()
xy_cor = list(zip(x_cor, y_cor))

districts_data_dict = dict(zip(districts_name, xy_cor))

game_is_on = True
correct_guesses = []
missing_districts = []

while game_is_on:
    answer_district = screen.textinput(title=f"{correct_answer}/64 districts Correct.",
                                       prompt="What's another district's name?").title()

    if answer_district in districts_data_dict and answer_district not in correct_guesses:
        correct_answer += 1
        correct_guesses.append(answer_district)

        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(districts_data_dict[answer_district])
        t.write(answer_district, align="center", font=FONT)
    if answer_district == "Exit":
        for district in districts_name:
            if district not in correct_guesses:
                missing_districts.append(district)
        new_data = pd.DataFrame(missing_districts, columns=["Missing Districts"])
        new_data.to_csv("Districts_to_learn.csv", index=False)
        break

screen.exitonclick()
