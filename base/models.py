'''
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

bank_name =(
    ('INDIAN BANK','INDIAN BANK'),
    ('STATE BANK OF INDIA','STATE BANK OF INDIA'),
    ('YES BANK','YES BANK'),
    ('INDIAN OVERSEAS BANK','INDIAN OVERSEAS BANK')
)

# Create your models here.

class Profile(models.Model):
    Aadharcard = models.IntegerField(validators=[MinLengthValidator(12)])
    Account_No = models.IntegerField(validators=[MinLengthValidator(15)])
    address = models.TextField(null=True)
    Mobile_No =  models.IntegerField()
    Date_of_Birth = models.DateField(max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.Username
    

class card(models.Model):
    card_no = models.IntegerField(validators=[MinLengthValidator(15)])
    expiry_date = models.DateField(max_length=8)
    card_holder = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.card_no[0:8]

class atm(models.Model):
    atm_id = models.IntegerField(validators=[MinLengthValidator(15)])
    transaction_id = models.IntegerField(validators=[MinLengthValidator(15)])
    amount = models.IntegerField(validators=[MinLengthValidator(1)])
    balance = models.CharField(max_length=25, blank=True, null=True)
    ifsc_code = models.IntegerField()
    bank = models.CharField(max_length=50,choices= bank_name)

    def __str__(self):
        return self.bank
'''