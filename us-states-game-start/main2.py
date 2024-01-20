import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv('50_states.csv')
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

CORRECT_GUESS_COUNT = 0
CORRECT_GUESSES = []


while CORRECT_GUESS_COUNT < 50:
    answer_state = screen.textinput(title=f'{CORRECT_GUESS_COUNT}/50 States Correct', prompt="What's another state's"
                                                                                              " name?").title()
    # Using list comprehension instead of for loops and if statements
    if answer_state == "Exit":
        states_to_learn = [state for state in states['state'] if state not in CORRECT_GUESSES]
        states_to_learn_data = pandas.DataFrame(states_to_learn)
        states_to_learn_data.to_csv('states_to_learn.csv')
        break
    for x in range(0, len(states)):
        if answer_state == states['state'][x]:
            CORRECT_GUESS_COUNT += 1
            CORRECT_GUESSES.append(answer_state)
            pen.goto(states['x'][x], states['y'][x])
            pen.write(answer_state, align='center', font=('Times New Roman', 9, 'normal'))






screen.exitonclick()