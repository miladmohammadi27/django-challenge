from rest_framework import serializers
from .models import Stadium, Team, Match


class StadiumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'

class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class MatchModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

    # represent name instead of id
    def to_representation(self, instance):
        representation = super(MatchModelSerializer, self).to_representation(instance)
        representation['stadium'] = instance.stadium.name
        representation['home_team'] = instance.home_team.name
        representation['guest_team'] = instance.guest_team.name
        return representation
