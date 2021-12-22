# Generated by Django 3.2.9 on 2021-12-22 12:40

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211222_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='PhoneNumberField',
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None, unique=True),
        ),
    ]