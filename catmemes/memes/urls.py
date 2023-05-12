from django.urls import path
from . import views

app_name = 'memes'

urlpatterns = [
    path('', views.MemeListView.as_view(), name='meme_list'),
    path('<int:pk>/', views.MemeDetailView.as_view(), name='meme_detail'),
]
