from functions.read_csv import read_csv

cases = ["/home/cani/workspace/civenjoyers-leaderboard/data/games.csv"]

for case in cases:
    print(read_csv(case))
