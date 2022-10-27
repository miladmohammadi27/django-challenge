from django.db import models
from uuid import uuid4
from jsonfield import JSONField
from django.db.models.signals import pre_save
from django.shortcuts import get_object_or_404


class Stadium(models.Model):
    name = models.CharField(max_length=50, verbose_name='Stadium Name')
    stadium_id = models.UUIDField(primary_key=True, editable=False, default=uuid4,
                                  unique=True, verbose_name='Stadium ID')
    seats = JSONField(verbose_name='Stadium Seats', default={
        "seats": []
    }
                      )

    class Meta:
        verbose_name = 'Stadium'
        verbose_name_plural = 'Stadiums'

    def __str__(self):
        return 'Stadium {}'.format(self.name)


class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name='Team Name')
    team_id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True, verbose_name='Team ID')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return '{} Volleybal Club'.format(self.name)


class Match(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, verbose_name='Stadium')
    match_id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True, verbose_name='Match ID')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Home Team',
                                  related_name='match_home_team')
    guest_team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Guest Team',
                                   related_name='match_guest_team')
    datetime = models.DateTimeField()
    sold_tickets = JSONField(verbose_name='Sold Tickets', editable=True)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

    def __str__(self):
        return 'Match Between {} VS {} In {} Stadium At {}'.format(
            self.stadium,
            self.home_team,
            self.guest_team,
            self.datetime,
        )

def match_pre_save(*args, **kwargs):
    stadium: Stadium = get_object_or_404(Stadium, stadium_id=kwargs.get('instance').stadium.stadium_id)
    seats_list: list = stadium.seats['seats']
    kwargs.get('instance').sold_tickets = dict.fromkeys(seats_list)


pre_save.connect(match_pre_save, sender=Match)
