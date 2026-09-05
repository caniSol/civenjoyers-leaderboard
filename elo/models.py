from django.db import models

from .functions.compute_elo import compute_elo
from .functions.update_wins import update_wins


class Player(models.Model):
    name = models.CharField(max_length=100)
    elo = models.IntegerField(default=1000)
    wins = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def update_elo(self, new_elo):
        self.elo = new_elo


class Game(models.Model):
    WINCONS = {
        "F": "Forefeit",
        "C": "Culture",
        "S": "Science",
        "R": "Religion",
        "D": "Diplomacy",
        "M": "Domination",
    }
    date = models.DateField()
    wincon = models.CharField(max_length=1, choices=WINCONS)
    place1 = models.ForeignKey(Player, on_delete=models.RESTRICT, related_name="+")
    place2 = models.ForeignKey(Player, on_delete=models.RESTRICT, related_name="+")
    place3 = models.ForeignKey(Player, on_delete=models.RESTRICT, related_name="+", blank=True, null=True)
    place4 = models.ForeignKey(Player, on_delete=models.RESTRICT, related_name="+", blank=True, null=True)
    place5 = models.ForeignKey(Player, on_delete=models.RESTRICT, related_name="+", blank=True, null=True)
    place6 = models.ForeignKey(Player, on_delete=models.RESTRICT, related_name="+", blank=True, null=True)
    place7 = models.ForeignKey(Player, on_delete=models.RESTRICT, related_name="+", blank=True, null=True)
    place8 = models.ForeignKey(Player, on_delete=models.RESTRICT, related_name="+", blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        for player in Player.objects.all():
            player.elo = 1000
            player.wins = 0
            player.save()

        for game in list(Game.objects.all()):
            compute_elo(game, Player.objects.all())

        update_wins(Player.objects.all(), Game.objects.all())
