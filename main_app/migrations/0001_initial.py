# Generated by Django 4.2.4 on 2023-08-22 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("date", models.DateTimeField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=19)),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[("debit", "Debit"), ("credit", "Credit")],
                        max_length=60,
                    ),
                ),
                (
                    "repeats",
                    models.CharField(
                        choices=[
                            ("once", "Once"),
                            ("weekly", "Weekly"),
                            ("biweekly", "Every Two Weeks"),
                            ("monthly", "Monthly"),
                        ],
                        max_length=60,
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.account",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main_app.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChildTransaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("date", models.DateTimeField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=19)),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[("debit", "Debit"), ("credit", "Credit")],
                        max_length=60,
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.account",
                    ),
                ),
                (
                    "transaction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="childtransactions",
                        to="main_app.transaction",
                    ),
                ),
            ],
        ),
    ]
