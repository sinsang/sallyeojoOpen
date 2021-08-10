from sallyeojo.settings import DEBUG
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Sum, Model
from .models import * 

# Create your views here.

copy = "Copyright 2021. sw980321 all rights reserved.<br/>sw980321@naver.com | 기록출처=<a href=\"http://www.statiz.co.kr/main.php\">STATIZ</a>"
teams = [i.name for i in Team.objects.all()]
description = "KBO 투수들의 혹사정도를 파악하는 살려조닷컴"
helpContent = "살려조 계산기는 KBO 투수들의 투구수, 연투, 휴식일을 기반으로 투수의 피로도(혹사도)를 측정하는 혹사랭킹 시스템입니다."
notice = "없음"

def main(req, season=2021):

    updateDate = UpdateDate.objects.values('update_date')[0]['update_date']

    players = TiredRecord.objects.select_related('player').filter(season=season).order_by('total_rank')
    availableSeasons = TiredRecord.objects.values('season').order_by('-season').distinct()

    for i in players:
        i.season_team_name = teams[i.season_team]
        i.pitcher_type = ["선발", "불펜"][i.pitcher_type]
        i.diff_total_rank = i.prev_total_rank - i.total_rank
        i.diff_pos_rank = i.prev_pos_rank - i.pos_rank

    return render(req, 'tiredRecord/main.html', {
        'DEBUG' : DEBUG,
        'description' : description,
        'players' : players, 
        'season' : season,
        'copyright' : copy,
        'updateDate' : updateDate,
        'availableSeasons' : availableSeasons,
        'helpContent' : helpContent,
        'notice' : notice,
    })


def playerSearch(req, player_name):

    playerSearchResults = Player.objects.all().filter(name__icontains=player_name).order_by("name")
    
    for i in playerSearchResults:
        i.team_name = teams[i.team]

    return render(req, 'tiredRecord/playerSearch.html', {
        'DEBUG' : DEBUG,
        'description' : description,
        'playerSearchResults' : playerSearchResults,
        'copyright' : copy,
        'helpContent' : helpContent,
        'notice' : notice,
    })


def playerRecord(req, player_id):

    playerInfo = Player.objects.get(pk=player_id)
    playerTiredRecord = TiredRecord.objects.all().filter(player=player_id).order_by("-season")

    playerInfo.team = teams[playerInfo.team]

    for i in playerTiredRecord:
        i.season_team_name = teams[i.season_team]
        i.pitcher_type = ["선발", "불펜"][i.pitcher_type]

    return render(req, 'tiredRecord/playerRecord.html', {
        'DEBUG' : DEBUG,
        'description' : description,
        'playerInfo' : playerInfo,
        'playerTiredRecord' : playerTiredRecord,
        'copyright' : copy,
        'helpContent' : helpContent,
        'notice' : notice,
    })


def teamsRecord(req, season):

    updateDate = UpdateDate.objects.values('update_date')[0]['update_date']

    teamsRecord = TiredRecord.objects.filter(season=season).values('season_team').annotate(Sum('tired_score'), Count("id")).order_by('-tired_score__sum')
    availableSeasons = TiredRecord.objects.values('season').order_by('-season').distinct()

    count = 1
    for i in teamsRecord:
        i['rank'] = count
        i['season_team_name'] = teams[i['season_team']]
        i['tired_score__sum'] = round(i['tired_score__sum'], 4)

        count += 1

    return render(req, 'tiredRecord/teamsRecord.html', {
        'DEBUG' : DEBUG,
        'description' : description,
        'season' : season,
        'teamsRecord' : teamsRecord,
        'availableSeasons' : availableSeasons,
        'updateDate' : updateDate,
        'copyright' : copy,
        'helpContent' : helpContent,
        'notice' : notice,
    })


def teamRecord(req, team_id, season=2021):
    
    updateDate = UpdateDate.objects.values('update_date')[0]['update_date']
    
    teamPlayerRecord = []
    if season == 0:
        teamPlayerRecord = TiredRecord.objects.select_related('player').filter(season_team=team_id).order_by('-tired_score')
    else:
        teamPlayerRecord = TiredRecord.objects.select_related('player').filter(season_team=team_id, season=season).order_by('-tired_score')

    count = 1
    pos_count = [1, 1]
    for i in teamPlayerRecord:
        i.total_rank = count
        i.pos_rank = pos_count[i.pitcher_type]
        count += 1
        pos_count[i.pitcher_type] += 1

        i.pitcher_type = ['선발', '불펜'][i.pitcher_type]

    availableSeasons = TiredRecord.objects.filter(season_team=team_id).values('season').order_by('-season').distinct()

    return render(req, 'tiredRecord/teamRecord.html', {
        'DEBUG' : DEBUG,
        'description' : description,
        'updateDate' : updateDate,
        'teamName' : teams[team_id],
        'teamId' : team_id,
        'teamPlayerRecord' : teamPlayerRecord,
        'availableSeasons' : availableSeasons,
        'season' : season,
        'copyright' : copy,
        'helpContent' : helpContent,
        'notice' : notice,
    })

