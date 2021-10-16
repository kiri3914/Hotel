from django.contrib import admin
from .models import CategoryRoom, CategoryFurniture, Room, Furniture

admin.site.register(CategoryFurniture)
admin.site.register(CategoryRoom)
admin.site.register(Room)
admin.site.register(Furniture)