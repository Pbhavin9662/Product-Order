from django.urls import path, include
from shop import views

urlpatterns = [
    path('', views.index, name="index"),
    path('order/', views.order, name="order"),
    path('update/<str:pk>/', views.update_order, name="update"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete"),
]
