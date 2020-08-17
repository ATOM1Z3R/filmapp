from rest_framework import serializers
from film.serializers import FilmListSerializer
from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    film = FilmListSerializer()
    class Meta:
        model = Genre
        fields = ['value', 'film']