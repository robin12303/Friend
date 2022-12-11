from django.db import models

class ParkingGuest(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    car_number_visit = models.CharField(max_length=20)
    phone_number_visit = models.FloatField()
    parking_state_visit = models.CharField(max_length=20)
    parking_entrance_time_visit = models.DateField()
    parking_exit_time_visit = models.DateField()
    address_visit = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'PARKING_GUEST'


class ParkingResident(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    car_number_resident = models.CharField(max_length=20)
    phone_number_resident = models.BigIntegerField()
    parking_state_resident = models.CharField(max_length=20)
    parking_exit_time_resident = models.DateField()

    class Meta:
        managed = False
        db_table = 'PARKING_RESIDENT'


class Resident(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    phone_number_resident = models.BigIntegerField()
    car_number_resident = models.CharField(max_length=15)
    address = models.CharField(max_length=15)
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'RESIDENT'