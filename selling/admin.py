from django.contrib import admin
from .models import Stadium, Team, Match

@admin.register(Stadium)
class StadiumsAdmin(admin.ModelAdmin):
    list_display = ('name', 'stadium_id')

@admin.register(Team)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_id')

@admin.register(Match)
class MatchesAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'guest_team', 'stadium', 'datetime')
