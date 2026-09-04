def update_wins(players, games) -> None:
    for game in games:
        winner = game.place1.name
        p = players.filter(name=winner)[0]
        p.wins += 1
        p.save()
