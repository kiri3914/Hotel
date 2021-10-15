from django.urls import path
from .views import *
urlpatterns = [
    path('category/furniture/list_create', CategoryFurnitureListCreateAPIView.as_view()),
    path('category/room/list_create', CategoryRoomListCreateAPIView.as_view()),
    path('furniture/list_create', FurnitureListCreateAPIView.as_view()),
    path('room/list_create', RoomListCreateAPIView.as_view()),
    path('category/room/detail/<int:pk>', CategoryRoomDetailAPIView.as_view()),
    path('category/furniture/detail/<int:pk>', CategoryFurnitureDetailAPIView.as_view()),
    path('furniture/detail/<int:pk>', FurnitureDetailAPIView.as_view()),
    path('room/detail/<int:pk>', RoomDetailAPIView.as_view()),
]