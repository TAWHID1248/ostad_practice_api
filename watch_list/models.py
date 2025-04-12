from django.db import models

# Create your models here.


class MovieList(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    movie = models.ForeignKey(MovieList, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.name} - {self.rating}"
