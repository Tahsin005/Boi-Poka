from django.db import models
from accounts.models import UserAccount
from . contants import TRANSACTION_TYPES
# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPES)