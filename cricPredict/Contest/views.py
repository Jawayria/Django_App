import datetime

# Create your views here.
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Contest.models import League, Match, Prediction, Score
from Contest.serializers import LeagueSerializer, MatchSerializer, PredictionSerializer, ScoreSerializer, \
    ExtendedMatchSerializer, ExtendedPredictionSerializer, ExtendedLeagueSerializer


class LeagueAPIView(APIView):
    permissions = (IsAuthenticated,)
    serializer_class = LeagueSerializer
    queryset = ''

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(groups = [])
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
        group = get_object_or_404(League, pk=pk)
        serializer = ExtendedLeagueSerializer(instance=group, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        League.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        group = get_object_or_404(League, pk=pk)
        serializer = ExtendedLeagueSerializer(instance=group, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class GroupLeaguesAPIView(APIView):
    permissions = (IsAuthenticated,)
    serializer_class = LeagueSerializer
    queryset = ''

    def get(self, request, pk):
        queryset = League.objects.filter(groups__in=[pk])
        queryset.order_by('start_date')
        serializer = LeagueSerializer(queryset, many=True)
        return Response(serializer.data)


class MatchAPIView(APIView):
    permissions = (IsAuthenticated,)
    serializer_class = MatchSerializer
    queryset = ''

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, pk=None):
        if pk is not None:
            queryset = Match.objects.get(pk=pk)
            queryset.order_by('time')
            serializer = ExtendedMatchSerializer(queryset)
        else:
            queryset = Match.objects.all()
            serializer = ExtendedMatchSerializer(queryset, many=True)

        return Response(serializer.data)

    def put(self, request, pk):
        group = get_object_or_404(Match, pk=pk)
        serializer = ExtendedMatchSerializer(instance=group, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Match.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        group = get_object_or_404(Match, pk=pk)
        serializer = ExtendedMatchSerializer(instance=group, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class LeagueMatchesAPIView(APIView):
    permissions = (IsAuthenticated,)
    serializer_class = ExtendedMatchSerializer
    queryset=''

    def get(self, request, pk):
        queryset = Match.objects.filter(league=pk)
        queryset.order_by('time')
        serializer = ExtendedMatchSerializer(queryset, many=True)
        return Response(serializer.data)


class PredictionAPIView(GenericAPIView):
    permissions = (IsAuthenticated,)
    serializer_class = PredictionSerializer
    queryset = ''

    def post(self, request, *args, **kwargs):
        serializerform = self.get_serializer(data=self.request.data)
        if not serializerform.is_valid():
            raise ParseError(detail="No valid values")
        else:
            match = Match.objects.get(id=request.data['match'])
            if request.data['prediction'] == match.team1 or request.data['prediction'] == match.team2:
                form = serializerform.save()
            else:
                raise ParseError(detail="This team is not playing")
        return Response(serializerform.data)

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params.get("id")
            if id is not None:
                prediction = Prediction.objects.get(id=id)
                serializer = ExtendedPredictionSerializer(prediction)

        except:
            result = Prediction.objects.all()
            serializer = ExtendedPredictionSerializer(result, many=True)
        return Response(serializer.data)


class ScoreAPIView(GenericAPIView):
    permissions = (IsAuthenticated,)
    serializer_class = ScoreSerializer
    queryset = ''

    def post(self, request, *args, **kwargs):
        serializerform = self.get_serializer(data=self.request.data)
        if not serializerform.is_valid():
            raise ParseError(detail="No valid values")
        else:
            form = serializerform.save()
        return Response(serializerform.data)

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id is not None:
                score = Score.objects.get(id=id)
                serializer = ScoreSerializer(score)

        except:
            result = Score.objects.all()
            serializer = ScoreSerializer(result, many=True)
        return Response(serializer.data)
