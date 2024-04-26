from django.db import models

class NbaTeam(models.Model):
    team_name = models.CharField(max_length=50)
    founded_year = models.IntegerField()
    championships_won = models.IntegerField()

    def __str__(self):
        return self.team_name
