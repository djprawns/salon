from __future__ import unicode_literals

from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Employee(models.Model):
    WEEKOFF_CHOICES = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THUR', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    )
    store = models.ForeignKey(Store)
    name = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    phone_no = models.IntegerField(default=0)
    address = models.CharField(max_length=200, null=True)
    doj = models.DateField(null=True)
    weekoff = models.CharField(max_length=4, choices=WEEKOFF_CHOICES, default=WEEKOFF_CHOICES[6][0])

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.name


# compute age during api call, however,
# actually storing the value will make
# sense in case of rolling out offers on birthdays
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    is_premium = models.BooleanField(default=False)
    email_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    MODE_CHOICES = (
        ('CASH', 'Cash'),
        ('CARD', 'Card Payment'),
        ('WALL', 'Mobile Wallet')
    )
    service = models.ManyToManyField(Service, default=None)
    customer = models.ForeignKey(Customer, default=0)
    employee = models.ForeignKey(Employee, default=0)
    amount = models.FloatField(default=0)
    payment_mode = models.CharField(max_length=4, choices=MODE_CHOICES, default=MODE_CHOICES[0][0])

    def __str__(self):
        return str(self.id)


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, default=0)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.id)
