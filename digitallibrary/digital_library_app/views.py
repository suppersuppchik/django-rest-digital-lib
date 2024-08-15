from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import viewsets
from django_filters import filterset

import django_filters


class BookFilter(django_filters.FilterSet):
    title = filterset.CharFilter(lookup_expr='icontains')
    author=filterset.CharFilter(field_name="author__fio",lookup_expr='icontains')
    class Meta:
        fields = [
            'title','author__fio'
        ]

@api_view(["GET", "POST"])
def crud_view(request):
    if request.method == "GET":
        if request_param := request.GET.get("search"):
            books = models.Book.objects.filter(title__icontains=request_param)
        else:
            books = models.Book.objects.all()
        serializer = serializers.ListBookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        serializer = serializers.CreateBookSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.craate_book_and_author(serializer.validated_data)
            print('VD', serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors,status=400)


class BookView(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filterset_class = BookFilter

    def list(self, request, *args, **kwargs):
        self.serializer_class = serializers.ListBookSerializer
        return super().list(request, *args, **kwargs)

    def get_object(self):
        self.serializer_class = serializers.DetailBookSerializer
        return super().get_object()

    def create(self, request, *args, **kwargs):
        self.serializer_class = serializers.CreateBookSerializer

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = serializers.UpdateBookSerializer
        return super().update(request, *args, **kwargs)
