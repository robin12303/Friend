# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Answer(models.Model):
    a_number = models.BigIntegerField(primary_key=True)
    b_number = models.ForeignKey('InquiryBoard', models.DO_NOTHING, db_column='b_number')
    a_writer = models.CharField(max_length=15)
    a_comment_date = models.DateField()
    a_content = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'ANSWER'


class Bill(models.Model):
    fee_number = models.BigIntegerField(primary_key=True)
    detailed_number = models.ForeignKey('Cost', models.DO_NOTHING, db_column='detailed_number')
    name = models.CharField(max_length=10)
    bill_year_month = models.BigIntegerField()
    calcul_start_date = models.DateField(blank=True, null=True)
    calcul_end_date = models.DateField()
    cutoff_date = models.DateField()
    import_status = models.CharField(max_length=10, blank=True, null=True)
    impose_finish = models.CharField(max_length=1, blank=True, null=True)
    arrears = models.BigIntegerField(blank=True, null=True)
    arrears_fine = models.BigIntegerField(blank=True, null=True)
    after_amount = models.BigIntegerField(blank=True, null=True)
    vbank = models.CharField(max_length=20)
    payment_method_id = models.CharField(max_length=10, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    late_fee = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BILL'


class Card(models.Model):
    payment_method_id = models.CharField(primary_key=True, max_length=20)
    id = models.CharField(max_length=15)
    card_number = models.BigIntegerField()
    valid_date = models.FloatField()
    card_cvc = models.FloatField()
    pay_method = models.FloatField()
    installment_plan = models.CharField(max_length=255)
    card_password = models.FloatField()

    class Meta:
        managed = False
        db_table = 'CARD'


class Cost(models.Model):
    detailed_number = models.BigIntegerField(primary_key=True)
    fee_number = models.BigIntegerField()
    address = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    general_cost = models.BigIntegerField()
    clean_cost = models.BigIntegerField()
    disinfect_cost = models.BigIntegerField()
    elevator_cost = models.BigIntegerField()
    guard_cost = models.BigIntegerField()
    fireenisurance_cost = models.BigIntegerField()
    commission_cost = models.BigIntegerField()
    electric_cost = models.BigIntegerField()
    allelectric_cost = models.BigIntegerField()
    tv_cost = models.FloatField()
    heating_cost = models.BigIntegerField()
    water_cost = models.BigIntegerField()
    allwater_cost = models.BigIntegerField()
    etc = models.CharField(max_length=20)
    repair_cost = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'COST'


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


class Operator(models.Model):
    oper_id = models.CharField(primary_key=True, max_length=20)
    oper_name = models.CharField(max_length=20)
    oper_tel = models.BigIntegerField(blank=True, null=True)
    oper_phone = models.BigIntegerField()
    oper_email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'OPERATOR'


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


class Payment(models.Model):
    fee_number = models.BigIntegerField(primary_key=True)
    amount = models.BigIntegerField()
    currency = models.CharField(max_length=10)
    pg = models.CharField(max_length=30)
    pay_method = models.CharField(max_length=30)
    card_installment = models.BigIntegerField()
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'PAYMENT'


class Receipt(models.Model):
    fee_number = models.BigIntegerField(primary_key=True)
    apply_number = models.BigIntegerField()
    re_name = models.CharField(max_length=20)
    pay_method = models.BigIntegerField()
    pay_amount = models.BigIntegerField()
    pg_id_number = models.CharField(max_length=20)
    pay_date = models.DateField()
    receipt_url = models.CharField(max_length=100)
    pay_name = models.CharField(max_length=20)
    pay_phone_number = models.CharField(max_length=20)
    pay_email = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    v_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'RECEIPT'


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


class Sms(models.Model):
    fee_number = models.BigIntegerField(primary_key=True)
    phone_number = models.BigIntegerField()
    from_number = models.BigIntegerField()
    content = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'SMS'












