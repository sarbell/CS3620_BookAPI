from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='action')
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fantasy')
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='mystery')
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='horror')
    serializer_class = BookSerializer


class HistoricalFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='historical-fiction')
    serializer_class = BookSerializer


class ClassicsViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='classics')
    serializer_class = BookSerializer


class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='science-fiction')
    serializer_class = BookSerializer


class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='biography')
    serializer_class = BookSerializer


class CookBookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='cook-books')
    serializer_class = BookSerializer


class KidsViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='kids')
    serializer_class = BookSerializer


