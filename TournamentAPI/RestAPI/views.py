from rest_framework import viewsets
from django.shortcuts import render
from django.views import View
from django.db import models
from .models import Tournament, Sections, Players, Games
from .serializers import TournamentSerializer, SectionsSerializer, PlayersSerializer, GamesSerializer

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    
class SectionsViewSet(viewsets.ModelViewSet):
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer


class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer

 


class RoundResultsView(View):
    def get(self, request):
        # Get the selected round from the query parameters (default to 1)
        round_number = int(request.GET.get('round', 1))
        
        # Get the highest round number present in the data
        highest_round = Games.objects.all().aggregate(max_round=models.Max('r1'))['max_round']
        
        # If there are no games, set highest_round to 1
        if highest_round is None:
            highest_round = 1
        
        # Get all games for the selected round, ordered by board number, excluding board -1
        round_games = Games.objects.filter(r1=round_number).exclude(board=-1).order_by('board')
        
        # Generate the range of rounds based on the highest round number
        rounds = range(1, highest_round + 1)
        
        context = {
            'round_number': round_number,
            'round_games': round_games,
            'rounds': rounds
        }
        return render(request, 'round_results.html', context)