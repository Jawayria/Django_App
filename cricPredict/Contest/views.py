from django.shortcuts import render
# Create your views here.
from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Contest.models import League, Match, Prediction, Score
from Contest.serializers import LeagueSerializer, MatchSerializer, PredictionSerializer, ScoreSerializer, \
    ExtendedMatchSerializer, ExtendedPredictionSerializer


class LeagueAPIView(GenericAPIView):
    permissions = (IsAuthenticated,)
    serializer_class = LeagueSerializer
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
                league = League.objects.get(id=id)
                serializer = LeagueSerializer(league)

        except:
            result = League.objects.all()
            serializer = LeagueSerializer(result, many=True)
        return Response(serializer.data)


class MatchAPIView(GenericAPIView):
    permissions = (IsAuthenticated,)
    serializer_class = MatchSerializer
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
                match = MatchAPIView.get()
                serializer = ExtendedMatchSerializer(match)

        except:
            matches = Match.objects.all()
            serializer = ExtendedMatchSerializer(matches, many=True)
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
