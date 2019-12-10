from django.contrib import admin

from .models import Room, Customer, Staff, ServiceType, Service

admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(ServiceType)
admin.site.register(Service)
