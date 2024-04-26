from django.core.management.base import BaseCommand
from nba.models import NbaTeam

class Command(BaseCommand):
    help = 'Seeds the database with NBA teams'

    def handle(self, *args, **options):
        teams = [
            {'team_name': 'Lakers', 'founded_year': 1947, 'championships_won': 17},
            {'team_name': 'Celtics', 'founded_year': 1946, 'championships_won': 17},
            {'team_name': 'Grizzlies', 'founded_year': 1995, 'championships_won': 0},
            {'team_name': 'Warriors', 'founded_year': 1946, 'championships_won': 6},
            {'team_name': 'Heat', 'founded_year': 1988, 'championships_won': 3}
        ]

        for team in teams:
            NbaTeam.objects.update_or_create(
                team_name=team['team_name'],
                defaults=team
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded NBA teams.'))

