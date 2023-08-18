from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Account, Transaction
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




def home(request):
    # Calculate the total balance of all accounts
    # Get user accounts

    context = {}

    if request.user.is_authenticated:
        accounts = Account.objects.filter(user=request.user)
        # get balances
        account_balances = [account.calculate_account_balance() for account in accounts]
        # total_balance 
        total_balance = sum(account_balances)

        # Retrieve all transactions for user
        transactions = Transaction.objects.filter(account__user=request.user)
        # transactions = Transaction.objects.order_by('date')
        context = {
            'total_balance': total_balance,
            'transactions': transactions,
        }
    return render(request, "home.html", context)


class AccountCreate(LoginRequiredMixin, CreateView):
    model = Account
    fields = "__all__"
    def get_initial(self):
        initial = super(AccountCreate, self).get_initial()
        initial['user'] = self.request.user
        return initial



class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    fields = ['name']


class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = "/"


class AccountDetail(LoginRequiredMixin, DetailView):
    model = Account
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the list of transactions for the account
        account = self.object
        transaction_list = Transaction.objects.filter(account=account)

        context['transaction_list'] = transaction_list
        return context


class AccountList(LoginRequiredMixin, ListView):
    model = Account
    fields = "__all__"


class TransactionCreate(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = "__all__"
    def get_initial(self):
        initial = super().get_initial()
        account_id = self.kwargs.get('account_id')
        account = Account.objects.get(id=account_id)
        initial['account'] = Account.objects.get(id=account_id)
        self.success_url = f"/accounts/{account_id}/"
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account_id = self.kwargs['account_id']
        context['account_id'] = account_id
        context['account'] = Account.objects.get(id=account_id)
        return context

    def get_form(self, form_class=None):
        form = super(TransactionCreate, self).get_form(form_class)
        # date field will otherwise be rendered as a regular input for no reason
        form.fields["date"].widget = AdminDateWidget(attrs={"type": "date"})
        return form


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



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
