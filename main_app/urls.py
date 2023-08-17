from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    #  accounts
    path("accounts/", views.AccountList.as_view(), name="account_list"),
    path("accounts/create/", views.AccountCreate.as_view(), name="account_create"),
    path(
        "accounts/<int:pk>/update", views.AccountUpdate.as_view(), name="account_update"
    ),
    path(
        "accounts/<int:pk>/delete", views.AccountDelete.as_view(), name="account_delete"
    ),
    path("accounts/<int:pk>/", views.AccountDetail.as_view(), name="account_detail"),
    path(
        "accounts/<int:pk>/transaction/create/",
        views.TransactionCreate.as_view(),
        name="transaction_create",
    ),
    path(
        "accounts/<int:pk>/transaction/delete/",
        views.TransactionDelete.as_view(),
        name="transaction_delete",
    ),
    path(
        "accounts/<int:pk>/transaction/update/",
        views.TransactionUpdate.as_view(),
        name="transaction_update",
    ),
   path('accounts/signup/', views.signup, name='signup'), 
]
