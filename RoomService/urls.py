from django.urls import path

from RoomService import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.CustomerView.as_view(), name='customer_view')
]
