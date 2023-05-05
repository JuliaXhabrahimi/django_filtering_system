# Generated by Django 4.2 on 2023-05-03 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("worker_filter", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Worker",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("user_type", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="job",
            name="worker",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="worker_filter.worker"
            ),
        ),
    ]
