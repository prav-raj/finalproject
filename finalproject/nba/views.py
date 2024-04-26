from django.shortcuts import render
from .models import NbaTeam

def nba_index(request):
    teams = NbaTeam.objects.all()
    return render(request, 'nba/nba_index.html', {'teams': teams})
