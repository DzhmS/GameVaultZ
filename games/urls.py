from django.urls import path

from . import views


urlpatterns = [
    path('', views.game_list, name='game-list'),
    path('create/', views.game_create, name='game-create'),
    path('<int:pk>/edit/', views.game_update, name='game-update'),
    path('<int:pk>/delete/', views.game_delete, name='game-delete'),
    path('<int:pk>/', views.game_detail, name='game-detail'),

    path('genres/', views.genre_list, name='genre-list'),
    path('genres/create/', views.genre_create, name='genre-create'),
    path('genres/<int:pk>/edit/', views.genre_update, name='genre-update'),
    path('genres/<int:pk>/delete/', views.genre_delete, name='genre-delete'),
    path('genres/<int:pk>/', views.genre_detail, name='genre-detail'),
]