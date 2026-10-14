from django.urls import path

from . import views


urlpatterns = [
    path('', views.platform_list, name='platform-list'),
    path('create/', views.platform_create, name='platform-create'),
    path('<int:pk>/edit/', views.platform_update, name='platform-update'),
    path('<int:pk>/delete/', views.platform_delete, name='platform-delete'),
    path('<int:pk>/', views.platform_detail, name='platform-detail'),
]