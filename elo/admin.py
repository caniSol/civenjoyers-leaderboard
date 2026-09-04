from django.contrib import admin

from .models import Player, Game


class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "elo",
        "wins",
    ]


class GameAdmin(admin.ModelAdmin):
    list_display = [
        "date",
        "wincon",
        "id",
        "place1",
    ]


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
