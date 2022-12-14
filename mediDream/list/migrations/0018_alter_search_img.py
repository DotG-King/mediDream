# Generated by Django 4.1.1 on 2022-12-02 04:13

from django.db import migrations, models
import list.models
import search.validators


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0017_alter_pillinfo_pill_effect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=list.models.date_upload_to, validators=[search.validators.validate_file]),
        ),
    ]
