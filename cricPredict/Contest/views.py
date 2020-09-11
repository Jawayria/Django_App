import datetime

# Create your views here.
from django.db.models import Sum
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Contest.models import League, Match, Prediction
from Contest.serializers import LeagueSerializer, MatchSerializer, PredictionSerializer, \
    ExtendedMatchSerializer, ExtendedPredictionSerializer, ExtendedLeagueSerializer, RankingsSerializer
from Groups.models import Group


class LeagueAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LeagueSerializer
    queryset = ''

    def post(self, request, *args, **kwargs):
        serializer = LeagueSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        if request.data['start_date'] < request.data['end_date']:
            serializer.save(groups=[])
        else:
            raise ParseError(detail="Dates are not valid")
        return Response(serializer.data)

    def get(self, request, pk=None):
        if pk is not None:
            queryset = League.objects.get(pk=pk)
            serializer = ExtendedLeagueSerializer(queryset)
        else:
            queryset = League.objects.filter(start_date__gte=datetime.date.today())
            queryset = queryset.order_by('start_date')
            serializer = ExtendedLeagueSerializer(queryset, many=True)

        return Response(serializer.data)

    def put(self, request, pk):
        league = get_object_or_404(League, pk=pk)
        serializer = ExtendedLeagueSerializer(instance=league, data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.data['start_date'] < request.data['end_date']:
            serializer.save()
        else:
            raise ParseError(detail="Dates are not valid")
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        League.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        league = get_object_or_404(League, pk=pk)
        serializer = ExtendedLeagueSerializer(instance=league, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if request.data['start_date'] < request.data['end_date']:
            serializer.save()
        else:
            raise ParseError(detail="Dates are not valid")
        return Response(status=status.HTTP_200_OK)


class GroupLeaguesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LeagueSerializer
    queryset = ''

    def get(self, request, pk):
        queryset = League.objects.filter(groups__in=[pk])
        queryset.order_by('start_date')
        serializer = LeagueSerializer(queryset, many=True)
        return Response(serializer.data)


class MatchAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MatchSerializer
    queryset = ''

    def post(self, request, *args, **kwargs):
        serializer = MatchSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, pk=None):
        if pk is not None:
            queryset = Match.objects.get(pk=pk)
            serializer = ExtendedMatchSerializer(queryset)
        else:
            queryset = Match.objects.all()
            queryset.order_by('time')
            serializer = ExtendedMatchSerializer(queryset, many=True)

        return Response(serializer.data)

    def put(self, request, pk):
        match = get_object_or_404(Match, pk=pk)
        serializer = ExtendedMatchSerializer(instance=match, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Match.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        match = get_object_or_404(Match, pk=pk)
        if 'winner' in request.data:
            if not (request.data['winner'] == match.team1 or request.data['winner'] == match.team2):
                request.data['winner'] = 'draw'
        serializer = ExtendedMatchSerializer(instance=match, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class LeagueMatchesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExtendedMatchSerializer
    queryset=''

    def get(self, request, pk):
        queryset = Match.objects.filter(league=pk)
        queryset.order_by('time')
        serializer = ExtendedMatchSerializer(queryset, many=True)
        return Response(serializer.data)


class PredictionAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PredictionSerializer
    queryset = ''

    def post(self, request, *args, **kwargs):
        serializer = PredictionSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        match = Match.objects.get(id=request.data['match'])
        group = Group.objects.get(id=request.data['group'])
        if not group.users.filter(id=request.data['user']).exists():
            raise ParseError(detail="User should be the member of group")
        if request.data['prediction'] == match.team1 or request.data['prediction'] == match.team2:
            form = serializer.save()
        else:
            raise ParseError(detail="This team is not playing")
        return Response(serializer.data)

    def get(self, request, pk=None):
        if pk is not None:
            queryset = Prediction.objects.get(pk=pk)
            serializer = ExtendedPredictionSerializer(queryset)
        else:
            queryset = Prediction.objects.all()
            serializer = ExtendedPredictionSerializer(queryset, many=True)

        return Response(serializer.data)

    def put(self, request, pk):
        prediction = get_object_or_404(Prediction, pk=pk)
        serializer = ExtendedPredictionSerializer(instance=prediction, data=request.data)
        serializer.is_valid(raise_exception=True)
        group = Group.objects.get(id=request.data['group'])
        if not group.users.filter(id=request.data['user']).exists():
            raise ParseError(detail="User should be the member of group")
        match = Match.objects.get(id=request.data['match'])
        if request.data['prediction'] == match.team1 or request.data['prediction'] == match.team2:
            form = serializer.save()
        else:
            raise ParseError(detail="This team is not playing")
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Prediction.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        prediction = get_object_or_404(Prediction, pk=pk)
        match = Match.objects.get(id=prediction.match.pk)
        if match.winner is not None and prediction.score is None:
            if match.winner == prediction.prediction:
                request.data['score'] = 3
            elif match.winner == 'draw':
                request.data['score'] = 0
            else:
                request.data['score'] = -1
        serializer = ExtendedPredictionSerializer(instance=prediction, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if 'prediction' in request.data:
            if request.data['prediction'] == match.team1 or request.data['prediction'] == match.team2:
                form = serializer.save()
            else:
                raise ParseError(detail="This team is not playing")
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class MatchPredictionsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExtendedPredictionSerializer
    queryset = ''

    def get(self, request, match, group):
        queryset = Prediction.objects.filter(match=match, group=group)
        queryset.order_by('time')
        serializer = ExtendedPredictionSerializer(queryset, many=True)
        return Response(serializer.data)


class UserPredictionsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExtendedPredictionSerializer
    queryset=''

    def get(self, request, user, league, group):
        matches = Match.objects.filter(league=league)
        groups = Group.objects.filter(id=group,users__in=[user])
        queryset = Prediction.objects.filter(user=user, match__in=matches, group__in=groups)
        serializer = ExtendedPredictionSerializer(queryset, many=True)
        return Response(serializer.data)


class RankingsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RankingsSerializer
    queryset=''

    def get(self, request, group, league):
        matches = Match.objects.filter(league=league)
        queryset = Prediction.objects.filter(group=group, match__in=matches)
        queryset = queryset.values('user').annotate(Sum('score')).order_by('-score__sum')
        serializer = RankingsSerializer(queryset, many=True)
        return Response(serializer.data)
