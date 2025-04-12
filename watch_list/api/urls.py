from django.urls import path
from .  import views


urlpatterns = [
    # path('', views.movie_list),
    # path('<pk>/', views.movie_details),
    path('', views.MovieListView.as_view()),
    path('<pk>/', views.MovieDetailView.as_view()),

    path('review/', views.ReviewListView.as_view()),
    path('review/<pk>/', views.ReviewDetailView.as_view()),
]