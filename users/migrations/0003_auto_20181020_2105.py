# Generated by Django 2.1.2 on 2018-10-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]