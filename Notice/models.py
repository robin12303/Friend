from django.db import models

# Create your models here.
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

class InquiryBoard(models.Model):
    b_number = models.BigIntegerField(primary_key=True)
    b_title = models.CharField(max_length=100, blank=True, null=True)
    b_pw = models.BigIntegerField()
    b_writer = models.CharField(max_length=15)
    b_content = models.CharField(max_length=2000)
    b_date = models.DateField()
    lock_flag = models.CharField(max_length=1)
    b_re_writer = models.CharField(max_length=15)
    b_re_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'INQUIRY_BOARD'


class Notice(models.Model):
    ntc_number = models.BigIntegerField(primary_key=True)
    ntc_title = models.CharField(max_length=100)
    ntc_txt = models.CharField(max_length=2000)
    ntc_writer = models.CharField(max_length=100)
    ntc_date = models.DateField()
    ntc_changer = models.CharField(max_length=100)
    ntc_change_date = models.DateField()
    ntc_reservation_notice = models.DateField()

    class Meta:
        managed = False
        db_table = 'NOTICE'