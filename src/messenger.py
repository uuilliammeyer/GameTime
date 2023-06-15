class Messenger:
    def __init__(self, games, heading, description):
        self.games = games
        self.heading = ""
        self.description = ""

    def create_notification(self) -> None:
        new_line = '\n'
        if len(self.games) == False:
            self.heading = "The Tigers do not play today :("
        else:
            if len(self.games) == 1:
                self.heading = str(self.games[0])
                # not sure if syntax here is right
                self.description = str(self.games[0].game_preview())
            else:
                self.heading = f"The Tigers play {len(self.games)} today!"
                description_string = ""
                for i in range(len(self.games)):
                    description_string += f"Game {i+1} @ {self.games[i].start_time}" + '\n' +f"{self.games[i].game_preview()}" + '\n'
                self.description = description_string
    
    def __str__(self):
        return f"Heading: {self.heading} Description: {self.description}"