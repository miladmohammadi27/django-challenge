from django.db import models
from uuid import uuid4
from jsonfield import JSONField
from django.shortcuts import get_object_or_404

"""
the selling app purpose is :
1- define stadiums for matches --> admins should do this
2- define teams for playing against each other --> admins should do this
3- define matches between two teams and in the one of defined stadiums --> admins should do this
4- view and buy seats by users to watch the match --> users should do this
"""

class Stadium(models.Model):
    name = models.CharField(max_length=50, verbose_name='Stadium Name')
    stadium_id = models.UUIDField(primary_key=True, editable=False, default=uuid4,
                                  unique=True, verbose_name='Stadium ID')

    # all available seats id or name, in the stadium should entered here as a list
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
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Home Team',
                                  related_name='match_home_team')
    guest_team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Guest Team',
                                   related_name='match_guest_team')
    datetime = models.DateTimeField()

    """
    a key value dictionary that represent :
    key ---> seat id or seat name 
    value ---> the user id for user that reserved the seat if None it means the seat is not reserved yet
    this field will be automatic generated based on stadium seats list when a new match defines
    """
    seats_reserve = JSONField(verbose_name='Seats And Reserving Status', editable=True)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

    def __str__(self):
        return 'Match Between {} VS {} In {} Stadium At {}'.format(
            self.home_team,
            self.guest_team,
            self.stadium,
            self.datetime,
        )

    # when a new match going to created seats_reserve field generated based on selected stadium seats list
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if not self.pk:
            stadium: Stadium = get_object_or_404(Stadium, stadium_id=self.stadium.stadium_id)
            seats_list: list = stadium.seats['seats']
            self.seats_reserve = dict.fromkeys(seats_list)
        super().save()

