from django.db import models
from statistics import mean
from django.contrib.auth.models import User
from genre.models import Genre
from director.models import Director


class Film(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=1200, blank=False)
    year = models.IntegerField(blank=False)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def avg_rating(self):
        rating = self.rating_set.all()
        try:
            avg = mean([item.value for item in rating])
        except:
            avg = None
        return avg

class Rating(models.Model):
    value = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True)