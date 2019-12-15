from django.urls import path

from RoomService import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:customer_id>/', views.customer_dashboard, name='customer-dashboard'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('service/request/<int:customer_id>/', views.customer_request_service, name='request-service'),
    path('customer/new/', views.customer_register, name='customer-register'),
    path('customer/edit/<int:customer_id>/', views.customer_update, name='customer-update'),
    path('service/cancel/<int:service_id>/', views.cancel_service, name='cancel-service'),
]
