from config import PATH_TO_GAMES_CSV, PATH_TO_LEADERBOARD_CSV, STANDARD_ELO
from functions.compute_elo import compute_elo
from functions.read_csv import read_csv


def main():
    print("Hello from civenjoyers-leaderboard!")
    games = read_csv(PATH_TO_GAMES_CSV)

    for game in games:
        compute_elo(game, PATH_TO_LEADERBOARD_CSV, STANDARD_ELO)

if __name__ == "__main__":
    main()
