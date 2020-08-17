from rest_framework.serializers import *
from django.contrib.auth.models import User
from .models import *


class UsernameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class FilmListSerializer(ModelSerializer):
    genre = PrimaryKeyRelatedField(queryset=Genre.objects.all())
    class Meta:
        model = Film
        fields = ['id','title','year','genre']

class FilmCreateSerializer(ModelSerializer):
    director = PrimaryKeyRelatedField(queryset=Director.objects.all())
    genre = PrimaryKeyRelatedField(queryset=Genre.objects.all())
    added_by = HiddenField(default=None)
    class Meta:
        model = Film
        fields = ['title','description','year','director','genre','added_by']

    def create(self, user, validated_data):
        validated_data['added_by'] = user
        return Film.objects.create(**validated_data)

class FilmDetailSerializer(ModelSerializer):
    added_by = UsernameSerializer(required=False)
    avg_rating = SerializerMethodField()
    genre = PrimaryKeyRelatedField(queryset=Genre.objects.all())
    director = PrimaryKeyRelatedField(queryset=Director.objects.all())
    class Meta:
        model = Film
        fields = ['title','description','year','director','genre','added_by', 'avg_rating']
        read_only_fields = ['date_added']
        depth = 1

    def get_avg_rating(self, obj):
        return obj.avg_rating

class RatingReadSerializer(ModelSerializer):
    film = FilmListSerializer()
    class Meta:
        model = Rating
        fields = ['id', 'value', 'film']
        depth = 1

class RatingSerializer(ModelSerializer):
    user = HiddenField(default=None)
    film = HiddenField(default=None)
    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, user, pk, validated_data):
        validated_data['user'] = user
        validated_data['film'] = Film.objects.get(pk=pk)
        return Rating.objects.create(**validated_data)

