from rest_framework import serializers
from . import models
from django.db import transaction

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
    author = AuthorSerializer()

    class Meta:
        model = models.Book
        fields = ["title", "author"]

    @transaction.atomic
    def craate_book_and_author(self, validated_data):
        author = models.Author.objects.create(**validated_data['author'])
        book = models.Book.objects.create(title=int(validated_data['title']),
                                          author=author)
        return book


class UpdateBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = ["title", "author"]


class DetailBookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = models.Book
        fields = ["id", "title", "author"]
