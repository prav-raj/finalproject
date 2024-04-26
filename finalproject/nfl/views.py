from django.shortcuts import render
from .models import NflTeam

def nfl_index(request):
    teams = NflTeam.objects.all()
    return render(request, 'nfl/nfl_index.html', {'teams': teams})
