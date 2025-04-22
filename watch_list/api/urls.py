from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .  import views

router = DefaultRouter()
router.register('movie', views.MovieListViewSet, basename='movie')
router.register('review', views.ReviewListViewSet, basename='review')

urlpatterns = [

    path('', include(router.urls)),


    # path('', views.movie_list),
    # path('<pk>/', views.movie_details),
    # path('', views.MovieListView.as_view()),
    # path('<pk>/', views.MovieDetailView.as_view()),

    # path('review/', views.ReviewListView.as_view()),
    # path('review/<pk>/', views.ReviewDetailView.as_view()),
]