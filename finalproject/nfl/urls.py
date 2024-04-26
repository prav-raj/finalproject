from django.urls import path
from .views import nfl_index

urlpatterns = [
    path('', nfl_index, name='nfl_index'),
]
