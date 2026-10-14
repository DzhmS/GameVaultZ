from django.urls import path

from . import views


urlpatterns = [
    path('', views.review_list, name='review-list'),
    path('create/', views.review_create, name='review-create'),
    path('<int:pk>/edit/', views.review_update, name='review-update'),
    path('<int:pk>/delete/', views.review_delete, name='review-delete'),
    path('<int:pk>/', views.review_detail, name='review-detail'),
]