# Generated by Django 4.1.1 on 2022-11-30 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0013_pillinfo_pill_ingredient_alter_pillinfo_pill_caution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillinfo',
            name='medication_information',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='pillinfo',
            name='pill_ingredient',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='pillinfo',
            name='pill_usage',
            field=models.TextField(max_length=5000),
        ),
    ]
