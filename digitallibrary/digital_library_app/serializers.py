from rest_framework import serializers
from . import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ["id", "fio"]


class ListBookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = models.Book
        fields = ["title", "author"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"


class CreateBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = ["title", "author"]


class UpdateBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = ["title", "author"]


class DetailBookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = models.Book
        fields = ["id", "title", "author"]
