from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from catalog.models import Book


class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)


class ReviewSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
    text = serializers.CharField()


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class BookSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    author = PrimaryKeyRelatedField(many=True, read_only=True)
    cover = serializers.ImageField(required=False)
    description = serializers.CharField()
    genre = PrimaryKeyRelatedField(many=True, read_only=True)
    # review = ReviewSerializer(many=True)

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        # instance.author = validated_data.get('author', instance.author)
        instance.cover = validated_data.get('cover', instance.cover)
        instance.description = validated_data.get('description', instance.description)
        instance.genre = validated_data.get('genre', instance.genre)
        # instance.review = validated_data.get('review', instance.review)
        instance.save()
        return instance
