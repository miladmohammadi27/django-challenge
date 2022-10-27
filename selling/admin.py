from django.contrib import admin
from .models import Stadium, Team, Match

@admin.register(Stadium)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'stadium_id')

@admin.register(Team)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_id')

@admin.register(Match)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'home_team', 'guest_team', 'stadium', 'datetime')
