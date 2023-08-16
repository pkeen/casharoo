from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/", views.AccountList.as_view(), name="accounts_list"),
    ]
