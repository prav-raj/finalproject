from django.db import models

class NflTeam(models.Model):
    team_name = models.CharField(max_length=50)
    head_coach = models.CharField(max_length=100)
    super_bowl_wins = models.IntegerField()

    def __str__(self):
        return self.team_name
