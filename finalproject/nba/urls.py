from django.urls import path
from .views import nba_index

urlpatterns = [
    path('', nba_index, name='nba_index'),
]
