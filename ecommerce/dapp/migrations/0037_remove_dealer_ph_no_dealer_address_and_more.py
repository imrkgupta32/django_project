# Generated by Django 4.2.3 on 2023-07-20 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dapp', '0036_remove_dealer_address_remove_dealer_nationality_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='ph_no',
        ),
        migrations.AddField(
            model_name='dealer',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dealer',
            name='nationality',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dealer',
            name='phone_no',
            field=models.CharField(blank=True, default='+977-', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='company',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='company_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='email_id',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='experience_years',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
