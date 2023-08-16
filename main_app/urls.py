from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    #  accounts
    path("accounts/", views.AccountList.as_view(), name="index"),
    path("accounts/create/", views.AccountCreate.as_view(), name="account_create"),
    path(
        "accounts/<int:pk>/update", views.AccountUpdate.as_view(), name="account_update"
    ),
    path(
        "accounts/<int:pk>/delete", views.AccountDelete.as_view(), name="account_delete"
    ),
    path("accounts/<int:pk>/", views.AccountDetail.as_view(), name="account_detail"),
]
