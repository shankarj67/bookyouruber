from django.urls import path, include
from . import views

urlpatterns = [
    path('findride/', views.book_ride, name="book_ride"),
]
