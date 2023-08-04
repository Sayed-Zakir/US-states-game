import turtle
import pandas as pd

data=pd.read_csv('50_states.csv')

screen=turtle.Screen()
screen.title('Guess the US states')
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:

    answer_state = screen.textinput(title=f'Guessed {len(guessed_states)}/50 US states', prompt="What's the name of the state").title()
    if answer_state=='Exit':
        missing_state=[]
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data=pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        turt=turtle.Turtle()
        turt.penup()
        turt.hideturtle()
        our_state=data[data.state==answer_state]
        turt.goto(int(our_state.x),int(our_state.y))
        turt.write(answer_state)
