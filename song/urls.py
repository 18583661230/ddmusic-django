from django.urls import path
from . import views

urlpatterns = [
    path('play', views.play_view),
    path('ranking_list', views.rank_view),
]
