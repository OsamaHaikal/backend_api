# Generated by Django 3.2.9 on 2022-01-01 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220101_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='store.product'),
        ),
    ]
