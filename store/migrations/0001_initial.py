# Generated by Django 3.2.9 on 2022-01-01 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_cart', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_by', models.CharField(max_length=100, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_by', models.CharField(max_length=100, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('price', models.PositiveIntegerField(default=0, null=True)),
                ('discount', models.IntegerField(blank=True, default=0, verbose_name='Discount percentage')),
                ('stock', models.IntegerField(blank=True, default=0)),
                ('available', models.BooleanField(default=True)),
                ('sizes', models.CharField(choices=[('1Kg', '1Kg'), ('2Kg', '2Kg')], default='1Kg', max_length=120)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('publish', 'publish')], default='draft', max_length=120)),
                ('image', models.ImageField(null=True, upload_to='media/images/')),
                ('category', models.ManyToManyField(blank=True, to='store.Category')),
            ],
            options={
                'ordering': ('created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_by', models.CharField(max_length=100, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_wishlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WishListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_by', models.CharField(max_length=100, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_product', to='store.product')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_items', to='store.wishlist')),
            ],
            options={
                'ordering': ('created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_by', models.CharField(max_length=100, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('name_of_receiver', models.CharField(max_length=100)),
                ('main_address', models.CharField(max_length=200)),
                ('secondary_address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('delivery_address', models.CharField(max_length=100, null=True)),
                ('postal_code', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=12)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_by', models.CharField(max_length=100, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('content', models.CharField(max_length=500)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckoutDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_by', models.CharField(max_length=100, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('name_of_receiver', models.CharField(max_length=100)),
                ('main_address', models.CharField(max_length=200)),
                ('secondary_address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('delivery_address', models.CharField(max_length=100, null=True)),
                ('postal_code', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=12)),
                ('cart', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checkout_details', to='store.cart')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('quantity', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='store.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='store.product')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
