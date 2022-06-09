from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over_message(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def start_message(self):
        self.home()
        self.write("Press 'space' to start.", align=ALIGNMENT, font=FONT)

    def show_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)
