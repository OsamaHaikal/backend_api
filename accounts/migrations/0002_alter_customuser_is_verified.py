# Generated by Django 3.2.9 on 2022-01-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]
