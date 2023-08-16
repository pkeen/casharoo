from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Account, Transaction


def home(request):
    return render(request, "home.html")


class AccountCreate(CreateView):
    model = Account
    fields = "__all__"


class AccountUpdate(UpdateView):
    model = Account
    fields = "__all__"

class AccountDelete(DeleteView):
    model = Account
    success_url = "/"


class AccountDetail(DetailView):
    model = Account

class AccountList(ListView):
    model = Account
    fields = "__all__"

class TransactionCreate(CreateView):
    model = Transaction
    fields = "__all__"


class TransactionUpdate(UpdateView):
    model = Transaction
    fields = "__all__"

class TransactionDelete(DeleteView):
    model = Transaction
    success_url = "/"

class TransactionDetail(DetailView):
    model = Transaction

class TransactionList(ListView):
    model = Transaction
    fields = "__all__"
