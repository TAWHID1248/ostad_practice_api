from . serializers import MovieListSerializer, ReviewSerializer
from watch_list import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework import generics

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = models.MovieList.objects.all() # python object 
#         serializer = MovieListSerializer(movies, many=True) # python object ke json e convert korbe
#         return Response(serializer.data)
#     else:
#         serializer = MovieListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
# # PUT --> [whole object kei pathate hoy]
# # PATCH --> [jei part ta update korte chai ta pathate hoy]
#     movie = get_object_or_404(models.MovieList, pk=pk)


#     if request.method == 'GET':
#         serializer = MovieListSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer = MovieListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     elif request.method == 'PATCH':
#         serializer = MovieListSerializer(movie, data=request.data, partial=True)
#         # partial=True mane holo je part ta update korte chai ta update hobe, baki thakbe
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response({'message': 'Movie deleted successfully!!'})


class MovieListView(generics.ListCreateAPIView):
    queryset = models.MovieList.objects.all()
    serializer_class = MovieListSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MovieList.objects.all()
    serializer_class = MovieListSerializer

class ReviewListView(generics.ListCreateAPIView):
    queryset = models.Reviews.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Reviews.objects.all()
    serializer_class = ReviewSerializer