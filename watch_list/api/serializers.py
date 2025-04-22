from rest_framework import  serializers

from watch_list import models



class  ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField()
    
    class Meta:
        model = models.Reviews
        fields = '__all__'



class MovieListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = models.MovieList

        fields = '__all__'