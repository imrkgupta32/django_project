# Generated by Django 4.2.3 on 2023-07-22 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_cart_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total',
            new_name='price',
        ),
    ]
