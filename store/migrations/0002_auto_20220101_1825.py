# Generated by Django 3.2.9 on 2022-01-01 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='checkoutdetails',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='checkoutdetails',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='review',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='shippingdetails',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='shippingdetails',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='updated_by',
        ),
    ]
