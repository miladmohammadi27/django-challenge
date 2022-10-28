from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics\
    import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Stadium, Team, Match
from . import serializers
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

"""stadium model CRUD API Views"""
class StadiumListCreate(ListCreateAPIView):
    model = Stadium
    serializer_class = serializers.StadiumModelSerializer
    http_method_names = ['post', 'get']
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Stadium.objects.all()


class StadiumRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.StadiumModelSerializer
    lookup_field = "stadium_id"
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Stadium.objects.all()
# ------------------------------------------------------------------------------------------


"""team model CRUD API Views"""
class TeamListCreate(ListCreateAPIView):
    model = Team
    serializer_class = serializers.TeamModelSerializer
    http_method_names = ['post', 'get']
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Team.objects.all()


class TeamRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TeamModelSerializer
    lookup_field = "team_id"
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Team.objects.all()
# ------------------------------------------------------------------------------------------


"""match model CRUD API Views"""
class MatchList(ListAPIView):
    model = Match
    serializer_class = serializers.MatchModelSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Match.objects.all()

class MatchRetrieve(RetrieveAPIView):
    serializer_class = serializers.MatchModelSerializer
    lookup_field = "id"
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Match.objects.all()

class MatchCreate(CreateAPIView):
    model = Match
    serializer_class = serializers.MatchModelSerializer
    http_method_names = ['post']
    permission_classes = [IsAdminUser]


class MatchRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MatchModelSerializer
    lookup_field = "id"
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Match.objects.all()
# ------------------------------------------------------------------------------------------


"""user buying seat API Views"""
class BuyingSeat(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user_id = request.user.id
        match_id = request.data['match_id']
        seat_id = request.data['seat_id']

        match = get_object_or_404(Match, pk=match_id)

        # if the seat id was not reserved by other user(seat is available)
        if not match.seats_reserve[seat_id]:
            match.seats_reserve.update({seat_id: user_id})
            match.save()
            return JsonResponse(
                {
                    "message": "Reserved Succeed For {}".format(match),
                    "Seat_id": seat_id
                }, status=status.HTTP_200_OK
            )
        else:
            return JsonResponse(
                {
                    "message": "Reserve Failed",
                    "reason": "The Seat Has Been Already Reserved"
                }, status=status.HTTP_400_BAD_REQUEST
            )




