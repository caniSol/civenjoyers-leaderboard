from config import PATH_TO_LEADERBOARD_CSV, STANDARD_ELO
from functions.compute_elo import compute_elo

case1 = {
    "PLACE_1": "Player1",
    "PLACE_2": "Player2",
    "PLACE_3": "Player3",
    "PLACE_4": "Player4",
}

case2 = {
    "PLACE_1": "Player4",
    "PLACE_2": "Player2",
    "PLACE_3": "Player3",
    "PLACE_4": "Player1",
}

print(compute_elo(case1, PATH_TO_LEADERBOARD_CSV, STANDARD_ELO))
print(compute_elo(case2, PATH_TO_LEADERBOARD_CSV, STANDARD_ELO))
