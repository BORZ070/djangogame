# Generated by Django 4.2.5 on 2023-12-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbot', '0008_supportq'),
    ]

    operations = [
        migrations.CreateModel(
            name='TSpam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='spam_image')),
            ],
        ),
    ]