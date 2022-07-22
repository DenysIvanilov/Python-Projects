import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states = pd.read_csv("50_states.csv")


guessed_list = []
while len(guessed_list) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_list)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in states["state"].unique() and answer_state not in guessed_list:
        guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    elif answer_state in guessed_list:
        pass
    if answer_state == "Exit":
        missing_states = []
        for state in states['state']:
            if state not in guessed_list:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


screen.exitonclick()
