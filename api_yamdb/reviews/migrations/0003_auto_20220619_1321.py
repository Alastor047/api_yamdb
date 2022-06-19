# Generated by Django 2.2.16 on 2022-06-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220619_1320'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='user',
            constraint=models.CheckConstraint(check=models.Q(username__iexact='me'), name='username_cannot_be_me'),
        ),
    ]