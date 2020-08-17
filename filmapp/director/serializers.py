from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Director
from film.serializers import FilmListSerializer


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class DirectorDetailSerializer(ModelSerializer):
    age = SerializerMethodField()
    film_set = FilmListSerializer(read_only=True, many=True)
    class Meta:
        model = Director
        fields = '__all__'

    def get_age(self, obj):
        return obj.age