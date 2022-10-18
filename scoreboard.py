from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            contents = file.read()
            self.high_score = int(contents)
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()
        pass

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", False, align="center", font=("Arial", 20, "normal"))
        
        
    def update_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", False, align="center", font=("Arial", 40, "normal"))