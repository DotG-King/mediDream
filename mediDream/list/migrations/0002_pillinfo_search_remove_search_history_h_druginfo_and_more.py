# Generated by Django 4.1.1 on 2022-11-22 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pillInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pill_name', models.CharField(max_length=50)),
                ('pill_effect', models.CharField(max_length=250)),
                ('pill_usage', models.CharField(max_length=250)),
                ('pill_caution', models.CharField(max_length=255)),
                ('pill_color', models.CharField(max_length=50)),
                ('pill_shape', models.CharField(max_length=50)),
                ('pill_engrave', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediDream_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.members')),
                ('pill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='list.pillinfo')),
            ],
        ),
        migrations.RemoveField(
            model_name='search_history',
            name='h_druginfo',
        ),
        migrations.RemoveField(
            model_name='search_history',
            name='h_id',
        ),
        migrations.DeleteModel(
            name='DRUGINFO',
        ),
        migrations.DeleteModel(
            name='Search_History',
        ),
    ]
