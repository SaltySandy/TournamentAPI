from django.db import models

class Tournament(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Sections(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='sections', on_delete=models.CASCADE, default=-1)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} - {self.tournament.title}"


class Players(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='players', on_delete=models.CASCADE, default=-1)
    section = models.ForeignKey(Sections, related_name='players', on_delete=models.CASCADE, null=True, blank=True)

    # Base information stored in a JSON field
    base = models.JSONField(default=dict)

    # Tournament-specific information stored in a JSON field
    tnmt = models.JSONField(default=dict)

    def __str__(self):
        return self.base.get('name', 'Unknown Player')


class Games(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='games', on_delete=models.CASCADE, default=-1)
    player1 = models.ForeignKey(Players, related_name='games_as_player1', on_delete=models.CASCADE, default=-1)
    player2 = models.ForeignKey(Players, related_name='games_as_player2', on_delete=models.CASCADE, default=-1)

    # Game fields with default values
    board = models.IntegerField(default=-1)
    color1 = models.IntegerField(default=0)
    color2 = models.IntegerField(default=0)
    p1 = models.IntegerField(default=-1)
    p2 = models.IntegerField(default=-1)
    r1 = models.IntegerField(default=-1)
    r2 = models.IntegerField(default=-1)
    result = models.FloatField(default=99)
    split = models.IntegerField(default=0)
    type = models.IntegerField(default=0)

    def __str__(self):
        return f"Game on board {self.board} with result {self.result}"
