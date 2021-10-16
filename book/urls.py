from django.urls import path
from .views import BookingListCreateAPIView, BookingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('booking/list_create', BookingListCreateAPIView.as_view()),
    path('booking/detail/<int:pk>', BookingRetrieveUpdateDestroyAPIView.as_view())
]