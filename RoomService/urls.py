from django.urls import path

from RoomService import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:customer_id>/', views.customer_dashboard, name='customer_view')
]
