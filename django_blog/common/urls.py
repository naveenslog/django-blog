from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name="category-list"),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name="category-detail")
]
