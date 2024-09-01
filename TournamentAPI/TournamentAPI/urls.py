from rest_framework.routers import DefaultRouter
from django.urls import path, include
from RestAPI.views import TournamentViewSet, SectionsViewSet, PlayersViewSet, GamesViewSet
from RestAPI.views import RoundResultsView


router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'sections', SectionsViewSet)
router.register(r'players', PlayersViewSet)
router.register(r'games', GamesViewSet)

urlpatterns = [
    path('', include(router.urls)),    
    path('round-results/', RoundResultsView.as_view(), name='round_results'),

]
