# Generated by Django 4.1.1 on 2022-11-22 01:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_pillinfo_search_remove_search_history_h_druginfo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
