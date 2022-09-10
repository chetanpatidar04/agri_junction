import email
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    mob_number = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    city = models.CharField(default="Shajapur", max_length=50)
    state = models.CharField(default='Madhya Pradesh', max_length=50)
    pincode = models.IntegerField(max_length=6)

    def register(self):
        self.save()
        return ("signup success")

    def isExists_email(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    def isExists_mob_number(self):
        if Customer.objects.filter(mob_number=self.mob_number):
            return True
        return False

    @staticmethod
    def get_customer_by_email(email_or_number):
        if email_or_number.isnumeric() and len(email_or_number) == 10:
            customer = Customer.objects.get(mob_number=email_or_number)
        else:
            customer = Customer.objects.get(email=email_or_number)
        return customer
