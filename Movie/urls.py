from django.urls import path
from Movie.views import *

urlpatterns = [
   path('movie/create/', MovieCreateView.as_view()),
   path('all/', MovieListView.as_view()),
   path('movie/detail/<int:pk>/', MovieDetailView.as_view()),
   path('feedback/create/', FeedbackCreateView.as_view()),
   path('rating/create/', RatingCreateView.as_view()),
   path('category/create/', CategoryCreateView.as_view()),
   path('actors/create/', ActorsCreateView.as_view()),
   path('staff/create/', StaffCreateView.as_view()),
   path('movieshots/create/', MovieShotsCreateView.as_view()),
   path('genre/create/', GenreCreateView.as_view()),
   path('starsrating/create/', StarsRatingCreateView.as_view()),
  ]