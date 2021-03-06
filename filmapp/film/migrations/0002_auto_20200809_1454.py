# Generated by Django 3.0.8 on 2020-08-09 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='poster',
        ),
        migrations.AddField(
            model_name='film',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='film',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='film.Film'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
