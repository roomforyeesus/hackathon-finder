# Generated by Django 4.1.1 on 2022-09-23 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0007_alter_subscriber_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscriber',
            new_name='Subscribers',
        ),
    ]
