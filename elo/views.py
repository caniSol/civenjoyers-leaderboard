from django.http import HttpResponse
from django.shortcuts import render

from .models import Player


def index(request):
    return HttpResponse("index")

def leaderboard(request):
    players = Player.objects.order_by("-elo")
    c = 1
    for player in players:
        player.place = c
        c += 1
    context = {"players": players}
    return render(request, "elo/leaderboard.html", context)
