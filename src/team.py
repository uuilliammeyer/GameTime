class Team:
    def __init__(self, team_name, wins, losses, probable_pitcher, ballpark, is_at_home):
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.probable_pitcher = probable_pitcher
        self.ballpark = ballpark
        self.is_at_home = is_at_home
        # 
    def  __str__(self):
        return f"The {self.team_name}, {self.wins}, {self.losses}, {self.probable_pitcher}, {self.ballpark}, {self.is_at_home}"
    