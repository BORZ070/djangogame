# Generated by Django 4.2.5 on 2023-11-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]