# Generated by Django 4.1.1 on 2022-11-30 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0012_alter_pillinfo_box_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pillinfo',
            name='pill_ingredient',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='pillinfo',
            name='pill_caution',
            field=models.TextField(max_length=50000),
        ),
    ]
