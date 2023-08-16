from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Account(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=19, decimal_places=2)

    def update_balance_from_transactions(self):
        # Fetch transactions that are in the past and haven't been processed
        transactions = self.transaction_set.filter(date__lte=timezone.now(), processed=False)
        
        for txn in transactions:
            if txn.amount > 0:
                self.balance += txn.amount  # for positive values, it's credited
            else:
                self.balance -= abs(txn.amount)  # for negative values, it's debited
            txn.processed = True
            txn.save()

        self.save()

class Transaction(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)  # can be positive (credit) or negative (debit)
    category = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    processed = models.BooleanField(default=False)

