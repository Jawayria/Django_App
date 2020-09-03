from django.shortcuts import render

# Create your views here.
from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Contest.models import League, Match, Prediction, Score
from Contest.serializers import LeagueSerializer, MatchSerializer, PredictionSerializer, ScoreSerializer


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
        result = Match.objects.all()
        serializer = MatchSerializer(result, many=True)
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
            form = serializerform.save()
        return Response(serializerform.data)

    def get(self, request, *args, **kwargs):
        result = Prediction.objects.all()
        serializer = PredictionSerializer(result, many=True)
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
        result = Score.objects.all()
        serializer = ScoreSerializer(result, many=True)
        return Response(serializer.data)