# Generated by Django 4.2.5 on 2024-03-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]