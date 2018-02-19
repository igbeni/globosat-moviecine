from rest_framework import serializers

from moviecine.models import Movie, Actor


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'image')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    actors = ActorSerializer(read_only=True, many=True)
    lookup_field = 'slug'
    extra_kwargs = {
        'url': {'lookup_field': 'slug'}
    }

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'original_title', 'synopsis', 'image', 'duration', 'published', 'slug', 'likes', 'actors')
