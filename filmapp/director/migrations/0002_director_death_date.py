# Generated by Django 3.0.8 on 2020-08-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='death_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
