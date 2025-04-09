from rest_framework import  serializers

from watch_list import models

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieList

        fields = '__all__'