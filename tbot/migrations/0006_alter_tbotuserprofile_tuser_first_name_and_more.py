# Generated by Django 4.2.5 on 2023-12-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbot', '0005_alter_tbotuserprofile_tuser_preference_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbotuserprofile',
            name='tuser_first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tbotuserprofile',
            name='tuser_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
