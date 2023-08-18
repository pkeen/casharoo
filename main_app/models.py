from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Account(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('account_detail', args=[str(self.id)])
    
    def calculate_account_balance(self):
        # method to calculate balance of account based on transaction history

        # Fetch transactions for account earlier than current date-time
        transactions = self.transaction_set.filter(date__lte=timezone.now())

        # Store for total
        balance = 0

        # iterate transactions
        for t in transactions:
            balance += t.amount

        return balance

        

class Transaction(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)  # can be positive (credit) or negative (debit)
    category = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

