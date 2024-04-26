from django.core.management.base import BaseCommand
from nfl.models import NflTeam

class Command(BaseCommand):
    help = 'Seeds the database with NFL teams'

    def handle(self, *args, **options):
        teams = [
            {'team_name': 'Patriots', 'head_coach': 'Bill Belichick', 'super_bowl_wins': 6},
            {'team_name': 'Packers', 'head_coach': 'Matt LaFleur', 'super_bowl_wins': 4},
            {'team_name': 'Titans', 'head_coach': 'Mike Vrabel', 'super_bowl_wins': 0},
            {'team_name': 'Cowboys', 'head_coach': 'Mike McCarthy', 'super_bowl_wins': 5},
            {'team_name': '49ers', 'head_coach': 'Kyle Shanahan', 'super_bowl_wins': 5}
        ]

        for team in teams:
            NflTeam.objects.update_or_create(
                team_name=team['team_name'],
                defaults=team
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded NFL teams.'))
