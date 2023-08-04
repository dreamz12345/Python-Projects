import turtle
import pandas


df = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("Guess US states Game!")
screen.bgpic("blank_states_img.gif")
drawing_turtle = turtle.Turtle(visible=False)
drawing_turtle.penup()

while not df.empty:
    title = f"{len(df)} states left"
    prompt = "Guess next state..."
    answer = screen.textinput(title, prompt).title()
    if answer in df.state.values:
        x = df[df.state == answer]["x"].values[0]  # Get xcor
        y = df[df.state == answer]["y"].values[0]  # Get ycor
        drawing_turtle.goto((x, y))
        drawing_turtle.write(answer)
        # Remove guessed state from DataFrame and fix indexes
        df = df[df.state != answer].reset_index(drop=True)

prompt_finish = "You named all states!"
font = ("Arial", 20, "normal")
drawing_turtle.goto((0, 250))
drawing_turtle.write(arg=prompt_finish, font=font, align="center")
screen.mainloop()
