# Generated by Django 4.2.5 on 2023-10-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_like_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(),
        ),
    ]
