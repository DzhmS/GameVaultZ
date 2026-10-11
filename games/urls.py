from django.urls import path

from . import views


urlpatterns = [
    path('', views.game_list, name='game-list'),
    path('create/', views.game_create, name='game-create'),
    path('<int:pk>/edit/', views.game_update, name='game-update'),
    path('<int:pk>/delete/', views.game_delete, name='game-delete'),
    path('<int:pk>/', views.game_detail, name='game-detail'),
]