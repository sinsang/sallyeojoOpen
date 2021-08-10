from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path("playerSearch/<str:player_name>", views.playerSearch, name="playerSearch"),        # 선수검색
    path('player/<int:player_id>', views.playerRecord, name="playerRecord"),                # 선수개인기록
    path('season/<int:season>', views.main, name="seasonRecord"),                           # 시즌별 선수기록
    path('teams/<int:season>', views.teamsRecord, name="teamsRecord"),                      # 시즌별 팀 기록
    path("team/<int:team_id>", views.teamRecord, name="teamRecordNow"),                     # 현 시즌 해당 팀 내 선수기록
    path("team/<int:team_id>/<int:season>", views.teamRecord, name="teamRecordPast")        # 시즌별 해당 팀 내 선수기록
]