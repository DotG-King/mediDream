# Generated by Django 4.1.1 on 2022-11-30 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0011_pillinfo_medication_information_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillinfo',
            name='box_picture',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pillinfo',
            name='pill_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
