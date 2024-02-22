import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import leaderboard, random


player = "Python Gamer"
score = 7 
print(leaderboard.save_player(player, score))

results = leaderboard.get_top()
if not results["success"]:
    print("error during fetch the top players")
else:
    for player in results["data"]:
        print(f"Player: {player['name']} score: {player['score']}")
    random_player = random.choice(results["data"])['name']
    random_player_info = leaderboard.get_player_score(random_player)
    print(random_player_info)
