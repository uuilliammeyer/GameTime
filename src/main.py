from datetime import datetime
# for Game object. Allows us to support double headers
from game import Game
from messenger import Messenger
import json 
import requests 
# team object helps organize team info
from team import Team

TIGERSNAME = "Detroit Tigers"
TODAY = datetime.today().strftime('%Y-%m-%d')
BASEURL = "https://baseballsavant.mlb.com/scoreboard-data?date="

def main():
    r = requests.get(BASEURL+TODAY)
    response_as_dict = json.loads(r.text)
    # initialize game id list. There might be double headers
    games = []
    for game_id in response_as_dict["games"]:
        # found game where tigers are either home or away
        if game_id["teams"]["home"]["name"] == TIGERSNAME or game_id["teams"]["away"]["name"] == TIGERSNAME:
            # initialize team objects for both teams 
            home_team = Team(
                team_name = game_id["teams"]["home"]["name"],
                wins = game_id["teams"]["home"]["record"]["wins"],
                losses = game_id["teams"]["home"]["record"]["losses"],
                probable_pitcher = game_id["probablePitchers"]["home"]["fullName"],
                ballpark = game_id["teams"]["home"]["venue"]["name"],
                is_at_home = True 
                )
            away_team = Team(
                team_name = game_id["teams"]["away"]["name"],
                wins = game_id["teams"]["away"]["record"]["wins"],
                losses = game_id["teams"]["away"]["record"]["losses"],
                probable_pitcher = game_id["probablePitchers"]["away"]["fullName"],
                ballpark = game_id["teams"]["away"]["venue"]["name"],
                is_at_home = False 
                )
            game = Game(
                home_team = home_team,
                away_team = away_team,
                start_time = game_id["datetime"]["time"] + " " + game_id["datetime"]["ampm"],
                ballpark = home_team.ballpark
            )
            games.append(game)
    for index, element in enumerate(games):
        print(f"Game {index+1}: {element}")
    messenger = Messenger(games, "", "")
    messenger.create_notification()
    print(messenger)

if __name__ == "__main__":
    main()
