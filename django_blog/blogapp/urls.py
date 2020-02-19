from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name="post-list"),
    path('post/<int:pk>/', views.PostDetail.as_view(), name="post-detail")
]
