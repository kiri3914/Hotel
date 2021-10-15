from rest_framework import serializers
from .models import CategoryRoom, CategoryFurniture, Furniture, Room


class CategoryRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryRoom
        fields = '__all__'


class CategoryFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryFurniture
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'
