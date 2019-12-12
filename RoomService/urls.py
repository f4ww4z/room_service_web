from django.urls import path

from RoomService import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:customer_id>/', views.customer_dashboard, name='customer-dashboard'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('service/request-service/', views.CustomerRequestServiceView.as_view(), name='request-service'),
]
