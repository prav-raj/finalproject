from django.contrib import admin
from django.urls import include, path
from home.views import welcome_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nba/', include('nba.urls')),
    path('nfl/', include('nfl.urls')),
    path('', welcome_view, name='home'),
]
