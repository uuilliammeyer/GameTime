class Game:
    def __init__(self, home_team, away_team, start_time, ballpark):
        self.home_team = home_team
        self.away_team = away_team
        self.start_time = start_time
        self.ballpark = ballpark

    def __str__(self):
        return f"The {self.home_team.team_name} take on the {self.away_team.team_name} at {self.start_time} in {self.ballpark}"
    
    def game_preview(self):
        preview = ""
        if self.home_team.team_name == "Detroit Tigers":
            preview = f"The {self.home_team.team_name} ({self.home_team.wins} - {self.home_team.losses}) \
                take on the {self.away_team.team_name} ({self.away_team.wins} - {self.away_team.losses}) today at home. \
                    The Tigers will likely start {self.home_team.probable_pitcher} against {self.away_team.probable_pitcher}"
        else:
            preview = f"The {self.away_team.team_name} ({self.away_team.wins} - {self.away_team.losses}) \
                faceoff against {self.home_team.team_name} ({self.home_team.wins} - {self.home_team.losses}) on the road at {self.home_team.ballpark}. \
                    The Tigers will likely start {self.away_team.probable_pitcher} against {self.home_team.probable_pitcher}"
        return preview

