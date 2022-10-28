from django.urls import path
from . import views


app_name = 'selling'

urlpatterns = [

    # User Must Have Admin Permission to Use This URLs
    path('stadium/listcreate/', views.StadiumListCreate.as_view(), name='stadium_listcreate'),
    path('stadium/rud/<str:stadium_id>', views.StadiumRetrieveUpdateDestroy.as_view(), name='stadium_rud'),
    # --------------------------------------------------------------------------------------------

    # User Must Have Admin Permission to Use This URLs
    path('team/listcreate/', views.TeamListCreate.as_view(), name='team_listcreate'),
    path('team/rud/<str:team_id>', views.TeamRetrieveUpdateDestroy.as_view(), name='team_rud'),
    # --------------------------------------------------------------------------------------------

    # User Must Be Authenticated To Use This URLs
    path('match/list/', views.MatchList.as_view(), name='match_list'),
    path('match/retrieve/<str:id>', views.MatchRetrieve.as_view(), name='match_retrieve'),

    # User Must Have Admin Permission to Use This URLs
    path('match/create/', views.MatchCreate.as_view(), name='match_create'),
    path('match/rud/<str:id>', views.MatchRetrieveUpdateDestroy.as_view(), name='match_rud'),
    # --------------------------------------------------------------------------------------------

    # User Must Be Authenticated To Use This URLs
    path('buy/seat/', views.BuyingSeat.as_view(), name='buy_seat'),

]
