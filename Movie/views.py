
from django.shortcuts import render
from rest_framework import generics
from Movie.serializers import *
from Movie.models import *
from Movie.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class MovieListView(generics.ListAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (TokenAuthentication, SessionAuthentication)


class FeedbackCreateView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer


class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer


class ActorsCreateView(generics.CreateAPIView):
    serializer_class = ActorsSerializer


class StaffCreateView(generics.CreateAPIView):
    serializer_class = StaffSerializer


class MovieShotsCreateView(generics.CreateAPIView):
    serializer_class = MovieShotsSerializer


class GenreCreateView(generics.CreateAPIView):
    serializer_class = GenreSerializer


class StarsRatingCreateView(generics.CreateAPIView):
    serializer_class = StarsRatingSerializer