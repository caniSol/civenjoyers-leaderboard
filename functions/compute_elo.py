from .read_csv import read_csv


def compute_elo(game: dict[str, str], PATH_TO_LEADERBOARD_CSV: str, STANDARD_ELO: int) -> None:
    elo_gain: dict[str, int] = {}

    for mate1, mate2 in compute_compare_options(game):
        old_elo_mate_1 = get_current_player_elo(mate1, PATH_TO_LEADERBOARD_CSV, STANDARD_ELO)
        old_elo_mate_2 = get_current_player_elo(mate2, PATH_TO_LEADERBOARD_CSV, STANDARD_ELO)

        new_elo_mate_1, new_elo_mate_2 = elo_rating(old_elo_mate_1, old_elo_mate_2)

        elo_gain[mate1] = new_elo_mate_1 - old_elo_mate_1
        elo_gain[mate2] = new_elo_mate_2 - old_elo_mate_2

    update_leaderboard(elo_gain, PATH_TO_LEADERBOARD_CSV, game["PLACE_1"])


def elo_rating(elo1: int, elo2: int, K: int = 30, outcome: int = 1) -> tuple[int, int]:
    # outcome: P1 win = 1, P2 win = 0

    prob2 = probability(elo1, elo2)
    prob1 = probability(elo2, elo1)

    new_elo1: int = round(elo1 + K * (outcome - prob1))
    new_elo2: int = round(elo2 + K * ((1 - outcome) - prob2))

    return new_elo1, new_elo2


def probability(elo1: int, elo2:int) -> float:
    return 1.0 / (1 + pow(10, (elo1 - elo2) / 400.0))


def compute_compare_options(game: dict[str, str]) -> list[tuple[str, str]]:
    standings = get_player_standings(game)
    matches: list[tuple[str, str]] = []

    for standing in standings:
        for i in range(standings.index(standing) + 1, len(standings)):
            matches.append((standing, standings[i]))

    return matches


def get_current_elo_board(PATH_TO_LEADERBOARD_CSV: str) -> dict[str, int]:
    leaderboard = read_csv(PATH_TO_LEADERBOARD_CSV)
    elo_board: dict[str, int] = {}

    for entry in leaderboard:
        elo_board[str(entry["NAME"])] = int(entry["ELO"])

    return elo_board


def get_current_player_elo(player: str, PATH_TO_LEADERBOARD_CSV: str, STANDARD_ELO: int) -> int:
    elo_board = get_current_elo_board(PATH_TO_LEADERBOARD_CSV)

    if player in elo_board:
        return elo_board[player]

    return STANDARD_ELO


def get_player_standings(game: dict[str, str]) -> list[str]:
    places = ["PLACE_1", "PLACE_2", "PLACE_3", "PLACE_4", "PLACE_5", "PLACE_6", "PLACE_7", "PLACE_8"]
    standings: list[str] = []

    for place in places:
        try:
            standings.append(game[place])
        except KeyError:
            break

    return standings

def update_leaderboard(elo_gain: dict[str, int], PATH_TO_LEADERBOARD_CSV: str, winning_player: str) -> None:
    leaderboard = read_csv(PATH_TO_LEADERBOARD_CSV)

    for player in leaderboard:
        if player["NAME"] in elo_gain:
            player["ELO"] = str(int(player["ELO"]) + int(elo_gain[player["NAME"]]))

            if player["NAME"] == winning_player:
                player["WINS"] = str(int(player["WINS"]) + 1)

    for player, value in elo_gain.items():
        found = False
        for entry in leaderboard:
            if entry["NAME"] == player:
                found = True

        if found == False:
            leaderboard.append({"NAME": player, "ELO": str(1000 + int(value)), "WINS": str(1 if winning_player == player else 0)})

    formatted_leaderboard: list[str] = ["NAME,ELO,WINS"]

    for entry in leaderboard:
        formatted_leaderboard.append(f"{entry['NAME']},{entry['ELO']},{entry['WINS']}")

    with open(PATH_TO_LEADERBOARD_CSV, "w") as leaderboard_csv:
        _ = leaderboard_csv.write("\n".join(formatted_leaderboard))
