def compute_probability(elo1: int, elo2: int) -> float:
    return 1.0 / (1 + pow(10, (elo1 - elo2) / 400.0))

def elo_comparison(elo1: int, elo2: int, K: int = 30, outcome: int = 1):
    prob2 = compute_probability(elo1, elo2)
    prob1 = compute_probability(elo2, elo1)

    gain1: int = round(K * (outcome - prob1))
    gain2: int = round(K * ((1 - outcome) - prob2))

    return gain1, gain2

def get_places_until_none(obj):
    places = []
    i = 1
    while True:
        attr_name = f'place{i}'
        value = getattr(obj, attr_name, None)
        if value is None:
            break
        places.append(value)
        i += 1
    return places

def compute_compare_options(game) -> list[tuple[str, str]]:
    standings = get_places_until_none(game)
    matches = []

    for standing in standings:
        for i in range(standings.index(standing) + 1, len(standings)):
            matches.append((standing, standings[i]))

    return matches

def apply_elo_gain(elo_gain, players):
    for player in elo_gain:
        player.elo = elo_gain[player] + player.elo
        player.save()

def compute_elo(game, players) -> None:
    elo_gain: dict[str, int] = {}

    for mate1, mate2 in compute_compare_options(game):
        old_elo_mate_1 = players.filter(name=mate1)[0].elo
        old_elo_mate_2 = players.filter(name=mate2)[0].elo

        elo_gain_1, elo_gain_2 = elo_comparison(old_elo_mate_1, old_elo_mate_2)

        if mate1 not in elo_gain:
            elo_gain[mate1] = elo_gain_1
        else:
            elo_gain[mate1] = elo_gain_1 + elo_gain[mate1]

        if mate2 not in elo_gain:
            elo_gain[mate2] = elo_gain_2
        else:
            elo_gain[mate2] = elo_gain_2 + elo_gain[mate2]

    apply_elo_gain(elo_gain, players)
