from rest_framework import serializers
from .models import Tournament, Sections, Players, Games
import time

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['board', 'color1', 'color2', 'player1', 'player2', 'r1', 'r2','p1', 'p2', 'result', 'split', 'type']


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ['base', 'tnmt']


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ['title']


class TournamentSerializer(serializers.ModelSerializer):
    sections = SectionsSerializer(many=True)
    players = PlayersSerializer(many=True)
    games = GamesSerializer(many=True)

    class Meta:
        model = Tournament
        fields = ['title', 'sections', 'players', 'games']

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        players_data = validated_data.pop('players')
        games_data = validated_data.pop('games')
        print(games_data)
        # time.sleep(3)
        tournament = Tournament.objects.create(**validated_data)

        # Create Sections
        for section_data in sections_data:
            Sections.objects.create(tournament=tournament, **section_data)

        # Create Players
        players = []
        for player_data in players_data:
            player = Players.objects.create(tournament=tournament, **player_data)
            players.append(player)

        # Create Games
        for game_data in games_data:
            player1_index = game_data['p1']
            player2_index = game_data['p2']
            game = Games.objects.create(
                tournament=tournament,
                player1=players[player1_index],
                player2=players[player2_index],
                **game_data
            )

        return tournament
