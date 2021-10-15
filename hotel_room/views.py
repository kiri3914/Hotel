from django.shortcuts import render
from .serializers import CategoryRoomSerializer, CategoryFurnitureSerializer, RoomSerializer, FurnitureSerializer
from .models import CategoryRoom, CategoryFurniture, Room, Furniture
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CategoryRoomListCreateAPIView(ListCreateAPIView):
    queryset = CategoryRoom.objects.all()
    serializer_class = CategoryRoomSerializer


class CategoryFurnitureListCreateAPIView(ListCreateAPIView):
    queryset = CategoryFurniture.objects.all()
    serializer_class = CategoryFurnitureSerializer


class RoomListCreateAPIView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class FurnitureListCreateAPIView(ListCreateAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer


class CategoryRoomDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryRoom.objects.all()
    serializer_class = CategoryRoomSerializer


class CategoryFurnitureDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryFurniture.objects.all()
    serializer_class = CategoryFurnitureSerializer


class RoomDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class FurnitureDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
