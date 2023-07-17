from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Room
from .serializers import RoomSerializer
# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    # ListAPIView is usually used for read only operations
    # class RoomViewSet(generics.ListAPIView):
    # ViewSets on the other hand are used for CRUD operations
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
