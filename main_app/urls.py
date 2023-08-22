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
        "accounts/<int:account_id>/transaction/create/",
        views.TransactionCreate.as_view(),
        name="transaction_create",
    ),
    path(
        "accounts/<int:account_id>/transaction/<int:pk>/delete/",
        views.TransactionDelete.as_view(),
        name="transaction_delete",
    ),
    path(
        "accounts/<int:account_id>/transaction/<int:pk>/update/",
        views.TransactionUpdate.as_view(),
        name="transaction_update",
    ),
   path('accounts/signup/', views.signup, name='signup'), 
   # Category Paths
   path('categories/', views.CategoryList.as_view(), name="category_list"),
   path('category/create/', views.CategoryCreate.as_view(), name="category_create"),
   path('category/<int:pk>/', views.CategoryDetail.as_view(), name="category_detail"),
   path('category/<int:pk>/update', views.CategoryUpdate.as_view(), name="category_update"),
   path("category/<int:pk>/delete", views.CategoryDelete.as_view(), name="category_delete"),
   path("expense_pie_chart/", views.ExpensePieChart, name="expense_pie_chart")
]
