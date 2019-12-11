from django.db import models


class Room(models.Model):
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=40)

    def __str__(self):
        return f'Room {self.room_number}, {self.room_type}'


class Customer(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=14)
    email = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name} - {self.contact_number}'


class Staff(models.Model):
    name = models.CharField(max_length=50, default='Fawwaz')
    contact_number = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    type = models.CharField(max_length=50)
    duration = models.TimeField('duration')

    def __str__(self):
        return self.type


class Service(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField('start_datetime')

    def __str__(self):
        start = self.start_datetime
        return f'{self.service_type} started on {start.ctime()}'
