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
        #TODO REMOVE THIS AFTER FEATURE IS COMPLETE
        return 42
        # method to calculate balance of account based on transaction history

        # Fetch transactions for account earlier than current date-time
        transactions = self.transaction_set.filter(date__lte=timezone.now())

        # Store for total
        balance = 0

        # iterate transactions
        for t in transactions:
            for ct in t.transaction_set.all():
                if ct.transaction_type == "debit":
                    balance -= ct.amount
                elif ct.transaction_type == "credit":
                    balance += ct.amount

        return balance


class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    REPEATS_TYPES = [("once", "Once"),("monthly","Monthly")]
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)  # can be positive (credit) or negative (debit)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True) # can be set to null and will be null if category deleted
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    repeats = models.CharField(max_length=60, choices=REPEATS_TYPES)

class ChildTransaction(models.Model):
    TRANSACTION_TYPES = [('debit', 'Debit'), ('credit', 'Credit')]
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    transaction_type = models.CharField(max_length=60, choices=TRANSACTION_TYPES)
