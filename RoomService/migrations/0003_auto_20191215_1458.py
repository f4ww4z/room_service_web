# Generated by Django 3.0 on 2019-12-15 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RoomService', '0002_staff_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RoomService.Customer'),
        ),
    ]
